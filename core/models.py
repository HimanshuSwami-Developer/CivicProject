from django.db import models


class Cause(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default="volunteer_activism")
    image_url = models.URLField(blank=True)
    goal_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    raised_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    @property
    def percent_funded(self):
        if not self.goal_amount:
            return 0
        return round(float(self.raised_amount) / float(self.goal_amount) * 100, 1)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "icon": self.icon,
            "image_url": self.image_url,
            "goal_amount": float(self.goal_amount),
            "raised_amount": float(self.raised_amount),
            "percent_funded": self.percent_funded,
        }


class Project(models.Model):
    STATUS_CHOICES = [
        ("on_track", "On Track"),
        ("at_risk", "At Risk"),
        ("completed", "Completed"),
    ]

    title = models.CharField(max_length=150)
    category = models.CharField(max_length=80, blank=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    goal_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    raised_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    progress_percent = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="on_track")
    priority = models.CharField(max_length=40, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "description": self.description,
            "image_url": self.image_url,
            "goal_amount": float(self.goal_amount),
            "raised_amount": float(self.raised_amount),
            "progress_percent": self.progress_percent,
            "status": self.status,
            "status_label": self.get_status_display(),
            "priority": self.priority,
            "is_featured": self.is_featured,
        }


class Donation(models.Model):
    STATUS_CHOICES = [
        ("success", "Success"),
        ("pending", "Pending"),
        ("failed", "Failed"),
    ]

    donor_name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    cause = models.ForeignKey(Cause, on_delete=models.SET_NULL, null=True, blank=True, related_name="donations")
    payment_method = models.CharField(max_length=40, blank=True, default="card")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="success")
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
            "amount": float(self.amount),
            "cause": self.cause.name if self.cause else "General Fund",
            "payment_method": self.payment_method,
            "status": self.status,
            "status_label": self.get_status_display(),
            "created_at": self.created_at.strftime("%b %d, %Y"),
        }


class Feedback(models.Model):
    TYPE_CHOICES = [
        ("suggestion", "Suggestion"),
        ("complaint", "Complaint"),
    ]
    STATUS_CHOICES = [
        ("new", "New"),
        ("in_review", "In Review"),
        ("resolved", "Resolved"),
        ("flagged", "Flagged"),
        ("approved", "Approved"),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    category = models.CharField(max_length=80, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_type_display()}: {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "email": self.email,
            "category": self.category,
            "message": self.message,
            "status": self.status,
            "status_label": self.get_status_display(),
            "response": self.response,
            "created_at": self.created_at.isoformat(),
        }


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    tags = models.CharField(max_length=200, blank=True)
    image_url = models.URLField(blank=True)
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
