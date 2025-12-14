from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_teacher

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_student

class IsParent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_parent


from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import IsTeacher, IsAdmin

class TeacherDashboardView(APIView):
    permission_classes = [IsTeacher]

    def get(self, request):
        return Response({"message": f"Welcome {request.user.username}, this is your dashboard."})

class AdminDashboardView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({"message": f"Welcome Admin {request.user.username}."})
