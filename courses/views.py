from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer
from users.permissions import IsTeacher

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacher]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']