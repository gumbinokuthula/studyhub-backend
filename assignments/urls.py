from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/', views.assignment_list, name='assignment_list'),
    path('create/<int:course_id>/', views.assignment_create, name='assignment_create'),
    path('detail/<int:id>/', views.assignment_detail, name='assignment_detail'),
]
