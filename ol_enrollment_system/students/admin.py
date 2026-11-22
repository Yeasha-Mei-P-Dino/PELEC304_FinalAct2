from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'full_name',
        'program',
        'year_level',
        'enrollment_status',
        'has_uploaded_pic',
    )
    search_fields = ('student_id', 'first_name', 'last_name', 'program')
    list_filter = ('enrollment_status', 'year_level')