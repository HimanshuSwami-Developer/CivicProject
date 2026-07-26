import json
import re

import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q, Sum
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

from .models import Donation, Feedback, GalleryImage, NewsArticle, YoutubeVideo, current_year

PAN_RE = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]$")
PAN_REQUIRED_ABOVE = 25000


def _body(request):
    if not request.body:
        return {}
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return {}


def _parse_year(request):
    raw = request.GET.get("year")
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError:
        return None


# ------------------------------------------------------------- donations ---

@require_http_methods(["GET"])
def donations_list(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)

    donations = Donation.objects.all()[:200]
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

    pan = (data.get("pan") or "").strip().upper()
    if amount > PAN_REQUIRED_ABOVE:
        if not pan:
            return JsonResponse({"error": "PAN is required for donations above ₹25,000"}, status=400)
        if not PAN_RE.match(pan):
            return JsonResponse({"error": "Invalid PAN format. Expected format: ABCDE1234F"}, status=400)

    client = _razorpay_client()
    if client is None:
        return JsonResponse({"error": "Online payments are not configured yet. Please try again later."}, status=503)

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
        pincode=(data.get("pincode") or "").strip(),
        state=(data.get("state") or "").strip(),
        city=(data.get("city") or "").strip(),
        pan=pan,
        amount=amount,
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

    return JsonResponse(donation.to_dict(), status=200)


@login_required
@require_http_methods(["GET"])
def donations_stats(request):
    agg = Donation.objects.filter(status="success").aggregate(total=Sum("amount"), donors=Count("id"))
    return JsonResponse({
        "total_collected": float(agg["total"] or 0),
        "active_donors": agg["donors"] or 0,
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

    articles = NewsArticle.objects.all()
    year = _parse_year(request)
    if year:
        articles = articles.filter(published_at__year=year)
    return JsonResponse({"results": [a.to_dict() for a in articles[:20]]})


# -------------------------------------------------------------- videos -----

@require_http_methods(["GET", "POST"])
def videos_list(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required"}, status=401)
        data = _body(request)
        video_id = (data.get("video_id") or "").strip()
        if not video_id:
            return JsonResponse({"error": "YouTube video ID is required"}, status=400)
        video = YoutubeVideo.objects.create(
            title=data.get("title") or "Untitled Video",
            video_id=video_id,
            thumbnail_url=data.get("thumbnail_url", ""),
            is_featured=data.get("is_featured", True),
            year=data.get("year") or current_year(),
        )
        return JsonResponse(video.to_dict(), status=201)

    videos = YoutubeVideo.objects.all()
    year = _parse_year(request)
    if year:
        videos = videos.filter(year=year)
    return JsonResponse({"results": [v.to_dict() for v in videos[:20]]})


@login_required
@require_http_methods(["DELETE"])
def video_detail(request, pk):
    try:
        video = YoutubeVideo.objects.get(pk=pk)
    except YoutubeVideo.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
    video.delete()
    return JsonResponse({"deleted": True})


# -------------------------------------------------------------- gallery ----

@require_http_methods(["GET", "POST"])
def gallery_list(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required"}, status=401)
        data = _body(request)
        image_url = (data.get("image_url") or "").strip()
        if not image_url:
            return JsonResponse({"error": "Image URL is required"}, status=400)
        image = GalleryImage.objects.create(
            image_url=image_url,
            caption=data.get("caption", ""),
            year=data.get("year") or current_year(),
        )
        return JsonResponse(image.to_dict(), status=201)

    images = GalleryImage.objects.all()
    year = _parse_year(request)
    if year:
        images = images.filter(year=year)
    return JsonResponse({"results": [i.to_dict() for i in images[:30]]})


@login_required
@require_http_methods(["DELETE"])
def gallery_detail(request, pk):
    try:
        image = GalleryImage.objects.get(pk=pk)
    except GalleryImage.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
    image.delete()
    return JsonResponse({"deleted": True})


@require_http_methods(["GET"])
def highlights_years(request):
    years = {current_year()}
    years.update(YoutubeVideo.objects.values_list("year", flat=True))
    years.update(GalleryImage.objects.values_list("year", flat=True))
    years.update(a.published_at.year for a in NewsArticle.objects.only("published_at"))
    return JsonResponse({"years": sorted(years, reverse=True)})


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
        "suggestions_count": suggestions_count,
        "complaints_count": complaints_count,
        "total_feedback": total_feedback,
        "resolution_rate": round((resolved_count / total_feedback * 100), 1) if total_feedback else 0,
        "recent_donations": [d.to_dict() for d in Donation.objects.all()[:5]],
        "recent_feedback": [f.to_dict() for f in Feedback.objects.all()[:5]],
        "articles": [a.to_dict() for a in NewsArticle.objects.all()[:3]],
    })
