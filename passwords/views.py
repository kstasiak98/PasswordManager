from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from passwords.forms import CustomUserCreationForm, PasswordCreate
from passwords.models import PasswordEntry
import ipdb


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


@login_required
def password_create(request):
    if request.method == "POST":
        form = PasswordCreate(request.POST, user=request.user)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner_password = request.user
            entry.save()
            messages.success(request, "Password saved successfully.")
            return redirect('home')
    else:
        form = PasswordCreate()
    return render(request, "password/password_create.html", {"form": form})


@login_required
def password_list(request):
    if request.method == 'POST' and request.is_ajax():
        user = request.user
        pk = request.POST.get('password_id')
        password = PasswordEntry.objects.get(pk=pk, owner_password=user)
        test = password.decrypt_password()
        return JsonResponse({'password': test}, status=200)
    user = request.user
    passwords = PasswordEntry.objects.filter(owner_password=user)
    return render(request, "password/password_list.html", {"passwords": passwords})

