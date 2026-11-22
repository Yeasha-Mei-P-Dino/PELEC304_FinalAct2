from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='student_profiles'),
    path('<int:student_id>/', views.profile_view, name='student_detail'),
    path('enroll/', views.enroll_student_view, name='enroll_student'),
]