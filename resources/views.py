from django.shortcuts import render, redirect
from .models import Course, Assignment
from django.contrib.auth.decorators import login_required

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    assignments = course.assignments.all()
    return render(request, 'courses/course_detail.html', {'course': course, 'assignments': assignments})
