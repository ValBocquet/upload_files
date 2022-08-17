from django.contrib import admin
from django.urls import path, include

from blog.views import HomeBlog

urlpatterns = [
    path('', HomeBlog.as_view(), name='home_blog'),
]