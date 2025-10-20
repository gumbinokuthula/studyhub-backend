from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Announcement
from courses.models import Course

@login_required
def announcement_list(request, course_id):
    course = Course.objects.get(id=course_id)
    announcements = Announcement.objects.filter(course=course).order_by('-created_at')
    return render(request, 'announcements/announcement_list.html', {'course': course, 'announcements': announcements})

@login_required
def announcement_create(request, course_id):
    course = Course.objects.get(id=course_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')
        
        if title and message:
            Announcement.objects.create(
                course=course,
                title=title,
                message=message,
                created_by=request.user
            )
            messages.success(request, "Announcement posted successfully!")
            return redirect('announcement_list', course_id=course.id)
        else:
            messages.error(request, "Both title and message are required.")
    
    return render(request, 'announcements/announcement_create.html', {'course': course})
