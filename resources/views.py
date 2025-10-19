from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Resource
from courses.models import Course
from django.contrib import messages

@login_required
def resource_list(request, course_id):
    course = Course.objects.get(id=course_id)
    resources = Resource.objects.filter(course=course)
    return render(request, 'resources/resource_list.html', {'course': course, 'resources': resources})

@login_required
def resource_upload(request, course_id):
    course = Course.objects.get(id=course_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        if title and file:
            Resource.objects.create(
                course=course,
                title=title,
                file=file,
                uploaded_by=request.user
            )
            messages.success(request, "Resource uploaded successfully!")
            return redirect('resource_list', course_id=course.id)
        else:
            messages.error(request, "Please provide a title and a file.")
    
    return render(request, 'resources/resource_upload.html', {'course': course})
