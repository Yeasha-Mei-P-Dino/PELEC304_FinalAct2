from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import OneTimeProfilePicForm, StudentEnrollmentForm
from .models import Student


def profile_view(request, student_id=None):
    search_query = request.GET.get('q', '').strip()
    students_qs = Student.objects.all()

    if search_query:
        students_qs = students_qs.filter(
            Q(first_name__icontains=search_query)
            | Q(last_name__icontains=search_query)
            | Q(student_id__icontains=search_query)
            | Q(program__icontains=search_query)
        )

    selected_student = None
    if student_id is not None:
        selected_student = get_object_or_404(Student, pk=student_id)
    elif students_qs.exists():
        selected_student = students_qs.first()
    elif Student.objects.exists():
        selected_student = Student.objects.first()

    if request.method == 'POST' and selected_student:
        if selected_student.has_uploaded_pic:
            messages.error(
                request,
                "Profile picture upload is locked because a photo was already saved."
            )
            return redirect('student_detail', student_id=selected_student.pk)

        form = OneTimeProfilePicForm(request.POST, request.FILES, instance=selected_student)
        if form.is_valid():
            student_obj = form.save(commit=False)
            student_obj.profile_pic_uploaded_at = timezone.now()
            student_obj.save()
            messages.success(
                request,
                "Profile picture uploaded! Because this is a one-time upload, it is now locked."
            )
            return redirect('student_detail', student_id=selected_student.pk)
        messages.error(request, "Please select a valid image file to upload.")
    else:
        form = OneTimeProfilePicForm(instance=selected_student)

    context = {
        'students': students_qs,
        'selected_student': selected_student,
        'form': form,
        'search_query': search_query,
        'active_page': 'profiles',
    }
    return render(request, 'students/profile_view.html', context)


def enroll_student_view(request):
    if request.method == 'POST':
        form = StudentEnrollmentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(
                request,
                f"Student {student.full_name} ({student.student_id}) has been added."
            )
            return redirect('student_detail', student_id=student.pk)
        messages.error(request, "Please fix the errors below before submitting.")
    else:
        form = StudentEnrollmentForm()

    return render(
        request,
        'students/enroll_student.html',
        {'form': form, 'active_page': 'enroll'},
    )