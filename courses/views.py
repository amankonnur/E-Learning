from django.shortcuts import render
from .forms import CourseForm
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