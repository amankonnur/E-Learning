from django.urls import path
from .views import add_course,course_details

urlpatterns = [
    path('coursedetails/',course_details,name = 'coursedetails'),
    path('addcourse/',add_course,name = 'addcourse')
]