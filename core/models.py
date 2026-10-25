from django.db import models
from django.contrib.auth.models import AbstractUser 


class CustomUser(AbstractUser):
    role = models.CharField(max_length=10,choices=[('Teacher', 'Teacher'), ('Student', 'Student')], default='Student')

    def __str__(self):
         return self.username
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
            return self.name
    

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(unique=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
       
    def __str__(self):
            return str(self.student)
    
    class Meta:
        models.UniqueConstraint(
            fields = ['student', 'course'],
            name = 'unique_student_course'
        )
    