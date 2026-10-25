from rest_framework.permissions import BasePermission

class Isowner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == object.student

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Teacher'

    def has_object_permission(self, request, view, obj):
        return request.user == object.teacher