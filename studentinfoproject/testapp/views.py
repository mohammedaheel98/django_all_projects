from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def student_info(request):
    #students = Student.objects.all()
    #students = Student.objects.filter(mark__lt=35)
    #students = Student.objects.filter(name__startswith='A')
    students = Student.objects.all().order_by('-mark')
    return render(request,'testapp/index.html',{'students':students})
