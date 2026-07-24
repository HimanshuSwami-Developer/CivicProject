from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


# --------------------------------------------------------- public (desktop)

@ensure_csrf_cookie
def landing(request):
    return render(request, "core/landing.html")


@ensure_csrf_cookie
def projects_page(request):
    return render(request, "core/projects.html")


@ensure_csrf_cookie
def donate_page(request):
    return render(request, "core/donate.html")


@ensure_csrf_cookie
def feedback_page(request):
    return render(request, "core/feedback.html")


# -------------------------------------------------------------- mobile app

@ensure_csrf_cookie
def app_home(request):
    return render(request, "core/app_home.html")


@ensure_csrf_cookie
def app_projects(request):
    return render(request, "core/app_projects.html")


@ensure_csrf_cookie
def app_donate(request):
    return render(request, "core/app_donate.html")


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
def admin_projects(request):
    return render(request, "core/admin_projects.html")
