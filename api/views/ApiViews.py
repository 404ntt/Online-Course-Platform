from rest_framework import generics
from api.serializers import MainSerilizers
from core.models import Lesson, Course, Enrollment, CustomUser
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from api.permissions.permissions import Isowner, IsTeacher


class CourseApiViewset(ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = MainSerilizers.CourseSerializer

class CourseApiView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = MainSerilizers.CourseSerializer
    permission_classes = [IsTeacher]

class LessonApiRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = MainSerilizers.LessonSerializer
    permission_classes = [IsTeacher]

class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = MainSerilizers.LessonSerializer
    permission_classes = [Isowner]

class EnrollmentApiListView(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = MainSerilizers.EnrollmentSerializer
    permission_classes = [Isowner]

class RegisterApiView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = MainSerilizers.RegisterSerializer

