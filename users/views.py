from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course

def dashboard_view(request):
    courses = Course.objects.all()
    return render(request, 'users/dashboard.html', {'courses': courses})


def courses_home(request):
    return HttpResponse("<h2>📚 Courses page coming soon!</h2>")

def assignments_home(request):
    return HttpResponse("<h2>📝 Assignments page coming soon!</h2>")

def resources_home(request):
    return HttpResponse("<h2>📂 Resources page coming soon!</h2>")

def announcements_home(request):
    return HttpResponse("<h2>📢 Announcements page coming soon!</h2>")


def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Welcome back!")
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You’ve been logged out.")
    return redirect('/users/dashboard/')

from django.shortcuts import render

def home_view(request):
    return render(request, 'users/home.html')
    
@login_required
def dashboard_view(request):
    courses = Course.objects.all()
    return render(request, 'users/dashboard.html', {'courses': courses})