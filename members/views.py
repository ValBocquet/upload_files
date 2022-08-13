from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'members/register.html'



def profil(request):
    return render(request, 'members/profil.html')


def logout(request):
    auth_logout(request)
    return render(request, 'home/home.html')
