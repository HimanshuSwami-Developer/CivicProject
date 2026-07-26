from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


# --------------------------------------------------------- public (desktop)

@ensure_csrf_cookie
def landing(request):
    return render(request, "core/landing.html")


@ensure_csrf_cookie
def about_page(request):
    return render(request, "core/about.html")


@ensure_csrf_cookie
def feedback_page(request):
    return render(request, "core/feedback.html")


# -------------------------------------------------------------- mobile app

@ensure_csrf_cookie
def app_home(request):
    return render(request, "core/app_home.html")


@ensure_csrf_cookie
def app_about(request):
    return render(request, "core/app_about.html")


@ensure_csrf_cookie
def app_feedback(request):
    return render(request, "core/app_feedback.html")


# ------------------------------------------------------------ admin panel

@ensure_csrf_cookie
@login_required
def admin_dashboard(request):
    return render(request, "core/admin_dashboard.html")


@ensure_csrf_cookie
@login_required
def admin_donations(request):
    return render(request, "core/admin_donations.html")


@ensure_csrf_cookie
@login_required
def admin_feedback(request):
    return render(request, "core/admin_feedback.html")


@ensure_csrf_cookie
@login_required
def admin_media(request):
    return render(request, "core/admin_media.html")
