from django.urls import path, include

from . import views

urlpatterns = [
    path('profil/', views.profil, name='profil'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]