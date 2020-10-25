from django.shortcuts import render, redirect
from django.contrib import messages
from passwords.forms import CustomUserCreationForm


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, "auth/register.html", {"form": form})
