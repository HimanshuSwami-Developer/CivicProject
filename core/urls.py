from django.contrib.auth import views as auth_views
from django.urls import path

from . import api, views

urlpatterns = [
    # public desktop site
    path("", views.landing, name="landing"),
    path("projects/", views.projects_page, name="projects"),
    path("donate/", views.donate_page, name="donate"),
    path("feedback/", views.feedback_page, name="feedback"),

    # mobile web app
    path("app/", views.app_home, name="app_home"),
    path("app/projects/", views.app_projects, name="app_projects"),
    path("app/donate/", views.app_donate, name="app_donate"),
    path("app/feedback/", views.app_feedback, name="app_feedback"),

    # admin panel
    path("admin-panel/login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="admin_login"),
    path("admin-panel/logout/", auth_views.LogoutView.as_view(next_page="admin_login"), name="admin_logout"),
    path("admin-panel/", views.admin_dashboard, name="admin_dashboard"),
    path("admin-panel/donations/", views.admin_donations, name="admin_donations"),
    path("admin-panel/feedback/", views.admin_feedback, name="admin_feedback"),
    path("admin-panel/projects/", views.admin_projects, name="admin_projects"),

    # JSON APIs
    path("api/causes/", api.causes_list, name="api_causes"),
    path("api/projects/", api.projects_list, name="api_projects"),
    path("api/projects/<int:pk>/", api.project_detail, name="api_project_detail"),
    path("api/donations/", api.donations_list, name="api_donations"),
    path("api/donations/stats/", api.donations_stats, name="api_donations_stats"),
    path("api/donations/create-order/", api.create_donation_order, name="api_donation_create_order"),
    path("api/donations/verify/", api.verify_donation_payment, name="api_donation_verify"),
    path("api/feedback/", api.feedback_list, name="api_feedback"),
    path("api/feedback/<int:pk>/", api.feedback_detail, name="api_feedback_detail"),
    path("api/news/", api.news_list, name="api_news"),
    path("api/dashboard/stats/", api.dashboard_stats, name="api_dashboard_stats"),
]
