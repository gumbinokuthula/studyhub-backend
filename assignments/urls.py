from django.urls import path
from . import views

urlpatterns = [
    # List assignments for a course
    path('<int:course_id>/', views.assignment_list, name='assignment_list'),

    # Create a new assignment for a course
    path('create/<int:course_id>/', views.assignment_create, name='assignment_create'),

    # Optional: view assignment details
    path('detail/<int:id>/', views.assignment_detail, name='assignment_detail'),
]
