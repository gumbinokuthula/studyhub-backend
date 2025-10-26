from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('<int:id>/', views.assignment_detail, name='assignment_detail'),
]
