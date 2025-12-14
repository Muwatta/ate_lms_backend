# classes/models.py
from django.db import models
from courses.models import Course
from users.models import User

class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"role": "student"})
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
