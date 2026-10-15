from rest_framework import generics
from api.serializers import MainSerilizers
from core.models import Lesson, Course

class CourseApiListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = MainSerilizers.CourseSerializer

class CourseApiRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = MainSerilizers.CourseSerializer


class LessonApiRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = MainSerilizers.LessonSerializer

class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = MainSerilizers.LessonSerializer
    