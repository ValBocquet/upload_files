from django.contrib import admin

# Register your models here.
from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "custom_user", "created_at")

    class Meta:
        ordering = "created_at"
