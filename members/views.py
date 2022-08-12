from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            messages.error(request, "Unsuccessful members. Invalid information.")
            return redirect('../profil/')
    form = RegisterForm()
    return render(request=request, template_name="members/register.html", context={"register_form": form})


def profil(request):
    return render(request, 'members/profil.html')


def logout(request):
    logout(request)
    messages.success(request, "Logout successful.")
    return render(request, 'home/home.html')
