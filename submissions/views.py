from django.shortcuts import render, redirect
from .models import Submission
from courses.models import Assignment
from django.contrib.auth.decorators import login_required

@login_required
def submit_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    if request.method == 'POST':
        file = request.FILES['file']
        Submission.objects.create(
            assignment=assignment,
            student=request.user,
            file=file
        )
        return redirect('course_detail', course_id=assignment.course.id)
    return render(request, 'submissions/submit_assignment.html', {'assignment': assignment})
