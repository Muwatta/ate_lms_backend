from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from datetime import datetime


from django.http import HttpResponse

def health_check(request):
    html_content = """
    <html>
        <head>
            <title>ATE LMS Backend</title>
            <style>
                body { font-family: 'Arial', sans-serif; text-align: center; padding: 50px; }
                .status { font-size: 2rem; color: green; }
                .details { margin-top: 20px; font-size: 1.2rem; }
            </style>
        </head>
        <body>
            <h1>ATE LMS Backend</h1>
            <div class="status">Status: OK</div>
            <div class="details">Service is live. API version: 1.0.0</div>
        </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path("api/auth/", include("users.urls")),

    # Core LMS
    path("api/courses/", include("courses.urls")),
    path("api/classes/", include("classes.urls")),
    path("api/assignments/", include("assignments.urls")),
    path("api/exams/", include("exams.urls")),
    path("api/grades/", include("grades.urls")),
    path("api/attendance/", include("attendance.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("", health_check),
]
