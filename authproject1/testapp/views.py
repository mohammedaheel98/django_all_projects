from django.http import HttpResponseRedirect
from testapp.forms import SignUpForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_view(request):
    return render(request,'testapp/java.html')

@login_required
def python_view(request):
    return render(request,'testapp/python.html')

@login_required
def django_view(request):
    return render(request,'testapp/django.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

def signup_form_view(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{"form":form})
