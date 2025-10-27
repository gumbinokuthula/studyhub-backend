from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/', views.resource_list, name='resource_list'),
    path('upload/<int:course_id>/', views.resource_upload, name='resource_upload'),
]
