from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import RegisterForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    return render(request, 'blog/profile.html')