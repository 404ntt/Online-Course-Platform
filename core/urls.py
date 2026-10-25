from django.urls import path
import core.views as views

urlpatterns = [
    path('', views.MainHome, name='home'),
    path('courses/', views.Courses.as_view(), name='courses'),
    path('course/<int:pk>/', views.Course_Detail.as_view(), name='course_detail'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('dashboard/<int:pk>/', views.Dashboard.as_view(), name='dashboard'),
    path('course/<int:pk>/join', views.enrollcourse, name='enroll'),
    path('course/<int:course_id>/lessoncreate', views.LessonCreateView.as_view(), name='create_lesson')
]