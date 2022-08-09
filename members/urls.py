from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.register_request, name='register_request'),
    path('', include("django.contrib.auth.urls")),
    path('profil/', views.profil, name='profil'),
]