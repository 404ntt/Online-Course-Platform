from django.shortcuts import render, redirect, resolve_url, get_object_or_404
import core.models as model
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from core.form import LoginForm, RegisterForm, CreateLesson, CreateCourseForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages

def MainHome(request):
    course = model.Course.objects.all()
    enroll = model.Enrollment.objects.filter(is_active=True)
    context = {
        'course': course,
        'enroll': enroll,
    }
    return render(request, 'core/home.html', context)



class Courses(generic.ListView):
    model = model.Course
    template_name = 'core/courses.html'
    context_object_name = 'course'


class Course_Detail(generic.DetailView):
    model = model.Course
    template_name = 'core/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self,**kwargs,):
        context = super().get_context_data(**kwargs)
        context['lesson'] = model.Lesson.objects.filter(course=self.object)
        context['is_enrolled'] = model.Enrollment.objects.filter(student=self.request.user, course=self.object).exists()
        context['custom'] = self.request.user
        return context


class Login(LoginView):
    authentication_form = LoginForm
    redirect_authenticated_user = True


class Logout(LogoutView):
    next_page = reverse_lazy('home')


class Register(generic.CreateView):
    template_name = 'core/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

class Dashboard(generic.DetailView):
    template_name = 'core/dashboard.html'
    model = model.CustomUser
    context_object_name = 'custom'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enroll'] = model.Enrollment.objects.all()
        return context

def enrollcourse(request, pk):
    if request.method != 'POST':
        return redirect('courses')
    course = get_object_or_404(model.Course, pk=pk, is_active=True)

    enroll, created = model.Enrollment.objects.get_or_create(student=request.user, course=course)

    if created:
        messages.success(request, 'Вы успешно записали на курс')
    else:
        messages.info(request, 'Вы уже записаны на курс')
    return redirect('course_detail', pk=course.pk)

class LessonCreateView(generic.CreateView):
    model = model.Lesson
    form_class = CreateLesson
    template_name = 'core/lesson_create.html'

    def form_valid(self, form):
        form.instance.course = get_object_or_404(
            model.Course, pk=self.kwargs['course_id']
        )
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('course_detail', kwargs={'pk': self.kwargs['course_id']})

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['Title'] = 'Dars'
            context['desc'] = 'Darsni'
            return context
class CourseCreateView(generic.CreateView):
    model = model.Course
    form_class = CreateCourseForm 
    template_name = 'core/lesson_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Kurs'
        context['desc'] = 'Kursni'
        return context

commit = []