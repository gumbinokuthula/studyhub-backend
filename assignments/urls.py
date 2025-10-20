from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/', views.assignment_list, name='assignment_list'),
    path('<int:course_id>/create/', views.assignment_create, name='assignment_create'),
]
