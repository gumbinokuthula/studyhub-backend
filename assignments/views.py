from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Assignment
from courses.models import Course
from django.contrib import messages

@login_required
def assignment_list(request, course_id):
    course = Course.objects.get(id=course_id)
    assignments = Assignment.objects.filter(course=course)
    return render(request, 'assignments/assignment_list.html', {'course': course, 'assignments': assignments})

@login_required
def assignment_create(request, course_id):
    course = Course.objects.get(id=course_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        
        if title and description and due_date:
            Assignment.objects.create(
                course=course,
                title=title,
                description=description,
                due_date=due_date,
                uploaded_by=request.user
            )
            messages.success(request, "Assignment created successfully!")
            return redirect('assignment_list', course_id=course.id)
        else:
            messages.error(request, "All fields are required.")
    
    return render(request, 'assignments/assignment_create.html', {'course': course})
