from django import forms
from core.models import CustomUser, Lesson, Course, Enrollment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class CreateLesson(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'order']