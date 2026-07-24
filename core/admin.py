from django.contrib import admin

from .models import Cause, Donation, Feedback, NewsArticle, Project


@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ("name", "goal_amount", "raised_amount", "is_active")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "progress_percent")
    list_filter = ("status", "category")


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("donor_name", "amount", "cause", "status", "created_at")
    list_filter = ("status", "cause")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "category", "status", "created_at")
    list_filter = ("type", "status")


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "views", "likes", "published_at")
