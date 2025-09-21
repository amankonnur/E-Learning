from .models import CourseDetails
from django import forms


class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseDetails
        fields = ['course_title', 'course_authour', 'course_description', 'course_price', 'course_thumbnail', 'course_duration']