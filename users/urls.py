from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('courses/', views.courses_home, name='courses_home'),
    path('assignments/', views.assignments_home, name='assignments_home'),
    path('resources/', views.resources_home, name='resources_home'),
    path('announcements/', views.announcements_home, name='announcements_home'),
]
