from django.shortcuts import render
from . import forms

# Create your views here.
def studentregistrationview(request):
    form = forms.StudentRegistration()
    return render(request,'testapp/index.html',{'form':form})
