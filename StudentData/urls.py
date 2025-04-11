from django.urls import path
from .views import StudentViewsData 

urlpatterns = [
    path("api/students/", StudentViewsData.as_view(), name="student-registration"),
]
