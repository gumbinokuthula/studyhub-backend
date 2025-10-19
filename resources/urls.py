from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/', views.resource_list, name='resource_list'),
    path('<int:course_id>/upload/', views.resource_upload, name='resource_upload'),
]
