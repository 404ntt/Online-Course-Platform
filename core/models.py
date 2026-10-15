from django.db import models
from django.contrib.auth.models import AbstractUser 

class CustomUser(AbstractUser):
    role = models.CharField(max_length=10,choices=[('teacher', 'Teacher'), ('student', 'Student')], default='student')
    added_at = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(null=False)
    added_at = models.DateTimeField(auto_now_add=True)

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
       

    class Meta:
        models.UniqueConstraint(
            fields = ['student', 'course'],
            name = 'unique_student_course'
        )
