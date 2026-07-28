from django.contrib.auth import views as auth_views
from django.urls import path

from . import api, views

urlpatterns = [
    # public desktop site
    path("", views.landing, name="landing"),
    path("about/", views.about_page, name="about"),
    path("feedback/", views.feedback_page, name="feedback"),

    # admin panel
    path("admin-panel/login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="admin_login"),
    path("admin-panel/logout/", auth_views.LogoutView.as_view(next_page="admin_login"), name="admin_logout"),
    path("admin-panel/", views.admin_dashboard, name="admin_dashboard"),
    path("admin-panel/donations/", views.admin_donations, name="admin_donations"),
    path("admin-panel/feedback/", views.admin_feedback, name="admin_feedback"),
    path("admin-panel/media/", views.admin_media, name="admin_media"),

    # JSON APIs
    path("api/donations/", api.donations_list, name="api_donations"),
    path("api/donations/stats/", api.donations_stats, name="api_donations_stats"),
    path("api/donations/create-order/", api.create_donation_order, name="api_donation_create_order"),
    path("api/donations/verify/", api.verify_donation_payment, name="api_donation_verify"),
    path("api/feedback/", api.feedback_list, name="api_feedback"),
    path("api/feedback/<int:pk>/", api.feedback_detail, name="api_feedback_detail"),
    path("api/news/", api.news_list, name="api_news"),
    path("api/videos/", api.videos_list, name="api_videos"),
    path("api/videos/<int:pk>/", api.video_detail, name="api_video_detail"),
    path("api/gallery/", api.gallery_list, name="api_gallery"),
    path("api/gallery/<int:pk>/", api.gallery_detail, name="api_gallery_detail"),
    path("api/highlights/years/", api.highlights_years, name="api_highlights_years"),
    path("api/dashboard/stats/", api.dashboard_stats, name="api_dashboard_stats"),
]
