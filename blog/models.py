from django.db import models
from django.template.defaultfilters import slugify

from members.models import CustomUser


class Article(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
