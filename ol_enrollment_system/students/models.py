from django.db import models


class Student(models.Model):
    STATUS_CHOICES = [
        ('Enrolled', 'Enrolled'),
        ('Pending', 'Pending'),
        ('For Review', 'For Review'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    ]

    # Enrollment & Identification
    student_id = models.CharField(max_length=25, unique=True)
    program = models.CharField(max_length=120)
    year_level = models.CharField(max_length=50)
    enrollment_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Pending'
    )
    date_enrolled = models.DateField(auto_now_add=True)

    # Personal Information
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=80)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, default='Male')
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    address = models.TextField()

    # Background Information
    previous_school = models.CharField(max_length=150)
    graduation_year = models.CharField(max_length=10)
    guardian_name = models.CharField(max_length=120)
    guardian_relationship = models.CharField(max_length=50, default='Parent/Guardian')
    guardian_contact = models.CharField(max_length=30)

    # One-Time Profile Picture
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    profile_pic_uploaded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    @property
    def full_name(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name[0]}. {self.last_name}"
        return f"{self.first_name} {self.last_name}"

    @property
    def has_uploaded_pic(self):
        return bool(self.profile_pic)

    def __str__(self):
        return f"{self.student_id} — {self.full_name}"