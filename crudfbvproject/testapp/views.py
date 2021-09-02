from testapp.forms import EmployeeForm
from django.shortcuts import redirect,render
from testapp.models import Employee
# Create your views here.

def retrive_view(request):
    employees = Employee.objects.all()
    return render(request,'testapp/index.html',{"employees":employees})

def create_view(request):
    form = EmployeeForm
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    return render(request,'testapp/create.html',{"form":form})

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    id = int(id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    id = int(id)
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        form.save(commit=True)
        return redirect('/')
    return render(request,'testapp/update.html',{"employee":employee})
