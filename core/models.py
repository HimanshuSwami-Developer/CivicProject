from django.db import models
from django.utils import timezone


def current_year():
    return timezone.now().year


class Member(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("contacted", "Contacted"),
        ("approved", "Approved"),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=80, blank=True)
    state = models.CharField(max_length=80, blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "city": self.city,
            "state": self.state,
            "pincode": self.pincode,
            "message": self.message,
            "status": self.status,
            "status_label": self.get_status_display(),
            "created_at": self.created_at.strftime("%b %d, %Y"),
        }


class Donation(models.Model):
    STATUS_CHOICES = [
        ("success", "Success"),
        ("pending", "Pending"),
        ("failed", "Failed"),
    ]

    donor_name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    state = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=80, blank=True)
    pan = models.CharField(max_length=10, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=40, blank=True, default="card")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="success")
    razorpay_order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.donor_name} - {self.amount}"

    def to_dict(self):
        return {
            "id": self.id,
            "donor_name": self.donor_name,
            "email": self.email,
            "phone": self.phone,
            "pincode": self.pincode,
            "state": self.state,
            "city": self.city,
            "pan": self.pan,
            "amount": float(self.amount),
            "payment_method": self.payment_method,
            "status": self.status,
            "status_label": self.get_status_display(),
            "created_at": self.created_at.strftime("%b %d, %Y"),
        }


class Feedback(models.Model):
    TYPE_CHOICES = [
        ("feedback", "Feedback"),
        ("complaint", "Complaint"),
    ]
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("resolved", "Resolved"),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=80, blank=True)
    state = models.CharField(max_length=80, blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    remark = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_type_display()}: {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "type_label": self.get_type_display(),
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "pincode": self.pincode,
            "message": self.message,
            "status": self.status,
            "status_label": self.get_status_display(),
            "remark": self.remark,
            "created_at": self.created_at.isoformat(),
        }


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    tags = models.CharField(max_length=200, blank=True)
    image_url = models.URLField(blank=True, max_length=500)
    category = models.CharField(max_length=60, blank=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "tags": self.tags,
            "image_url": self.image_url,
            "category": self.category,
            "views": self.views,
            "likes": self.likes,
            "published_at": self.published_at.strftime("%b %d, %Y"),
        }


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=30)
    thumbnail_url = models.URLField(blank=True, max_length=500)
    is_featured = models.BooleanField(default=True)
    year = models.PositiveIntegerField(default=current_year)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-year", "-published_at"]

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "video_id": self.video_id,
            "thumbnail_url": self.thumbnail_url or f"https://img.youtube.com/vi/{self.video_id}/hqdefault.jpg",
            "url": f"https://www.youtube.com/watch?v={self.video_id}",
            "is_featured": self.is_featured,
            "year": self.year,
            "published_at": self.published_at.strftime("%b %d, %Y"),
        }


class GalleryImage(models.Model):
    image_url = models.URLField(max_length=500)
    caption = models.CharField(max_length=200, blank=True)
    year = models.PositiveIntegerField(default=current_year)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-year", "-uploaded_at"]

    def __str__(self):
        return self.caption or f"Gallery image #{self.pk}"

    def to_dict(self):
        return {
            "id": self.id,
            "image_url": self.image_url,
            "caption": self.caption,
            "year": self.year,
            "uploaded_at": self.uploaded_at.strftime("%b %d, %Y"),
        }
