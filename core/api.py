import json

import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q, Sum
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

from .models import Cause, Donation, Feedback, NewsArticle, Project


def _body(request):
    if not request.body:
        return {}
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return {}


# ---------------------------------------------------------------- causes ---

@require_http_methods(["GET"])
def causes_list(request):
    causes = Cause.objects.filter(is_active=True)
    return JsonResponse({"results": [c.to_dict() for c in causes]})


# -------------------------------------------------------------- projects ---

@require_http_methods(["GET", "POST"])
def projects_list(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required"}, status=401)
        data = _body(request)
        project = Project.objects.create(
            title=data.get("title", "Untitled Initiative"),
            category=data.get("category", ""),
            description=data.get("description", ""),
            image_url=data.get("image_url", ""),
            goal_amount=data.get("goal_amount") or 0,
            raised_amount=data.get("raised_amount") or 0,
            progress_percent=data.get("progress_percent") or 0,
            status=data.get("status", "on_track"),
            priority=data.get("priority", ""),
        )
        return JsonResponse(project.to_dict(), status=201)

    projects = Project.objects.all()
    featured = request.GET.get("featured")
    if featured:
        projects = projects.filter(is_featured=True)
    return JsonResponse({"results": [p.to_dict() for p in projects]})


@require_http_methods(["GET", "PATCH"])
@login_required
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    if request.method == "PATCH":
        data = _body(request)
        for field in ("title", "category", "description", "image_url", "status", "priority"):
            if field in data:
                setattr(project, field, data[field])
        for field in ("goal_amount", "raised_amount", "progress_percent"):
            if field in data:
                setattr(project, field, data[field])
        project.save()

    return JsonResponse(project.to_dict())


# ------------------------------------------------------------- donations ---

@require_http_methods(["GET"])
def donations_list(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)

    donations = Donation.objects.select_related("cause").all()[:200]
    return JsonResponse({"results": [d.to_dict() for d in donations]})


def _razorpay_client():
    if not settings.RAZORPAY_KEY_ID or not settings.RAZORPAY_KEY_SECRET:
        return None
    return razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


@require_http_methods(["POST"])
def create_donation_order(request):
    data = _body(request)

    try:
        amount = float(data.get("amount"))
    except (TypeError, ValueError):
        amount = 0
    if amount <= 0:
        return JsonResponse({"error": "A valid donation amount is required"}, status=400)

    donor_name = (data.get("donor_name") or "").strip()
    email = (data.get("email") or "").strip()
    phone = (data.get("phone") or "").strip()
    if not donor_name or not email or not phone:
        return JsonResponse({"error": "Full name, email and phone number are required"}, status=400)

    client = _razorpay_client()
    if client is None:
        return JsonResponse({"error": "Online payments are not configured yet. Please try again later."}, status=503)

    cause = None
    cause_id = data.get("cause_id")
    if cause_id:
        cause = Cause.objects.filter(pk=cause_id).first()

    amount_paise = int(round(amount * 100))
    try:
        order = client.order.create({
            "amount": amount_paise,
            "currency": "INR",
            "payment_capture": 1,
        })
    except Exception:
        return JsonResponse({"error": "Could not start the payment. Please try again."}, status=502)

    donation = Donation.objects.create(
        donor_name=donor_name,
        email=email,
        phone=phone,
        state=(data.get("state") or "").strip(),
        city=(data.get("city") or "").strip(),
        amount=amount,
        cause=cause,
        payment_method="razorpay",
        status="pending",
        razorpay_order_id=order["id"],
    )

    return JsonResponse({
        "donation_id": donation.id,
        "order_id": order["id"],
        "amount": amount_paise,
        "currency": "INR",
        "key": settings.RAZORPAY_KEY_ID,
        "name": donor_name,
        "email": email,
        "phone": phone,
    }, status=201)


@require_http_methods(["POST"])
def verify_donation_payment(request):
    data = _body(request)
    donation_id = data.get("donation_id")
    order_id = data.get("razorpay_order_id")
    payment_id = data.get("razorpay_payment_id")
    signature = data.get("razorpay_signature")

    if not all([donation_id, order_id, payment_id, signature]):
        return JsonResponse({"error": "Missing payment details"}, status=400)

    try:
        donation = Donation.objects.get(pk=donation_id, razorpay_order_id=order_id)
    except (Donation.DoesNotExist, ValueError):
        return JsonResponse({"error": "Donation not found"}, status=404)

    client = _razorpay_client()
    if client is None:
        return JsonResponse({"error": "Online payments are not configured yet."}, status=503)

    try:
        client.utility.verify_payment_signature({
            "razorpay_order_id": order_id,
            "razorpay_payment_id": payment_id,
            "razorpay_signature": signature,
        })
    except razorpay.errors.SignatureVerificationError:
        donation.status = "failed"
        donation.save(update_fields=["status"])
        return JsonResponse({"error": "Payment verification failed"}, status=400)

    donation.status = "success"
    donation.razorpay_payment_id = payment_id
    donation.save(update_fields=["status", "razorpay_payment_id"])

    if donation.cause:
        donation.cause.raised_amount = float(donation.cause.raised_amount) + float(donation.amount)
        donation.cause.save(update_fields=["raised_amount"])

    return JsonResponse(donation.to_dict(), status=200)


@login_required
@require_http_methods(["GET"])
def donations_stats(request):
    agg = Donation.objects.filter(status="success").aggregate(total=Sum("amount"), donors=Count("id"))
    return JsonResponse({
        "total_collected": float(agg["total"] or 0),
        "active_donors": agg["donors"] or 0,
        "causes": [c.to_dict() for c in Cause.objects.filter(is_active=True)],
    })


# -------------------------------------------------------------- feedback ---

@require_http_methods(["GET", "POST"])
def feedback_list(request):
    if request.method == "POST":
        data = _body(request)
        message = data.get("message")
        if not message:
            return JsonResponse({"error": "Message is required"}, status=400)
        feedback = Feedback.objects.create(
            type=data.get("type", "suggestion"),
            name=data.get("name") or "Anonymous",
            email=data.get("email", ""),
            category=data.get("category", ""),
            message=message,
            status="pending",
        )
        return JsonResponse(feedback.to_dict(), status=201)

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)

    feedback = Feedback.objects.all()
    feedback_type = request.GET.get("type")
    if feedback_type:
        feedback = feedback.filter(type=feedback_type)
    return JsonResponse({"results": [f.to_dict() for f in feedback]})


@login_required
@require_http_methods(["GET", "PATCH"])
def feedback_detail(request, pk):
    try:
        feedback = Feedback.objects.get(pk=pk)
    except Feedback.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    if request.method == "PATCH":
        data = _body(request)
        if "status" in data:
            valid_statuses = {choice for choice, _ in Feedback.STATUS_CHOICES}
            if data["status"] not in valid_statuses:
                return JsonResponse({"error": "Invalid status"}, status=400)
            feedback.status = data["status"]
        if "response" in data:
            feedback.response = data["response"]
        feedback.save()

    return JsonResponse(feedback.to_dict())


# --------------------------------------------------------------- news ------

@require_http_methods(["GET", "POST"])
def news_list(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required"}, status=401)
        data = _body(request)
        article = NewsArticle.objects.create(
            title=data.get("title", "Untitled Article"),
            content=data.get("content", ""),
            tags=data.get("tags", ""),
            image_url=data.get("image_url", ""),
            category=data.get("category", ""),
        )
        return JsonResponse(article.to_dict(), status=201)

    articles = NewsArticle.objects.all()[:20]
    return JsonResponse({"results": [a.to_dict() for a in articles]})


# ------------------------------------------------------------ dashboard ----

@login_required
@require_http_methods(["GET"])
def dashboard_stats(request):
    donation_agg = Donation.objects.filter(status="success").aggregate(total=Sum("amount"))
    suggestions_count = Feedback.objects.filter(type="suggestion").count()
    complaints_count = Feedback.objects.filter(type="complaint").count()
    total_feedback = suggestions_count + complaints_count
    resolved_count = Feedback.objects.filter(status__in=["resolved", "approved"]).count()

    return JsonResponse({
        "total_donations": float(donation_agg["total"] or 0),
        "active_projects": Project.objects.exclude(status="completed").count(),
        "suggestions_count": suggestions_count,
        "complaints_count": complaints_count,
        "total_feedback": total_feedback,
        "resolution_rate": round((resolved_count / total_feedback * 100), 1) if total_feedback else 0,
        "recent_donations": [d.to_dict() for d in Donation.objects.all()[:5]],
        "recent_feedback": [f.to_dict() for f in Feedback.objects.all()[:5]],
        "articles": [a.to_dict() for a in NewsArticle.objects.all()[:3]],
    })
