from django.shortcuts import render
from .forms import CourseForm
from .models import CourseDetails
# Create your views here.


def add_course(request):
    if request.POST:
        courseform = CourseForm(request.POST,request.FILES)
        if courseform.is_valid():
            courseform.save()
            courseform = CourseForm()
        else:
            print(courseform.errors)
    else:
        courseform = CourseForm()

    return render(request,'courses/courseform.html',{'courseform':courseform})


def course_details(request):
    allcourses = CourseDetails.objects.all()
    print(allcourses)
    return render(request,'courses/course_details.html',{'allcourses':allcourses})