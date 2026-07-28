from django.contrib import admin

from .models import Donation, Feedback, GalleryImage, NewsArticle, YoutubeVideo


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("donor_name", "amount", "status", "created_at")
    list_filter = ("status",)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "phone", "status", "created_at")
    list_filter = ("type", "status")


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "views", "likes", "published_at")


@admin.register(YoutubeVideo)
class YoutubeVideoAdmin(admin.ModelAdmin):
    list_display = ("title", "video_id", "year", "is_featured", "published_at")
    list_filter = ("year", "is_featured")


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("caption", "year", "uploaded_at")
    list_filter = ("year",)
