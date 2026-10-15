from rest_framework import serializers
from core import models

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'