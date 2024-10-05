from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the input is an email or username
        try:
            user = User.objects.get(email=username_or_email)
            username = user.username
        except User.DoesNotExist:
            username = username_or_email
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'users/login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # All the necessary validations. (confirm password, taken username, already in use email)
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'users/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return render(request, 'users/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return render(request, 'users/signup.html')

        # Create the user if all of the above validations are passed.
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully!")
            return redirect('login')
        except ValidationError as e:
            messages.error(request, e)
            return render(request, 'users/signup.html')

    return render(request, 'users/signup.html')

# Below functions require authentication.

@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html', {'username': request.user.username})

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def change_password_view(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        
        if new_password == confirm_new_password and request.user.check_password(old_password):
            request.user.set_password(new_password)
            request.user.save()
            return redirect('dashboard') 
    return render(request, 'users/change_password.html')


# WhatBytes Assignment by Anant Singh.