from testapp.models import Employee
from django.shortcuts import render

# Create your views here.
def employee_info(request):
    employees = Employee.objects.all()
    return render(request,'testapp/results.html',{'employees':employees})