from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/', views.announcement_list, name='announcement_list'),
    path('<int:course_id>/create/', views.announcement_create, name='announcement_create'),
]
