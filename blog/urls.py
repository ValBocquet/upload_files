from django.contrib import admin
from django.urls import path, include

from blog.views import HomeBlog, DisplayArticle

urlpatterns = [
    path('', HomeBlog.as_view(), name='home_blog'),
    path('<str:slug>/', DisplayArticle.as_view(), name="article"),
]