from django.shortcuts import render
from testapp.forms import *
# Create your views here.
def name_view_form(request):
    form = NameForm()
    return render(request,'testapp/name.html',{'form':form})

def age_view_form(request):
    form = AgeForm()
    name = request.GET["name"]
    request.session["name"] = name
    return render(request,'testapp/age.html',{"form":form})

def prof_view_from(request):
    form = ProfForm()
    age = request.GET["age"]
    request.session["age"] = age
    return render(request,'testapp/prof.html',{"form":form})

def result_view(request):
    profession = request.GET["profession"]
    request.session["profession"] = profession
    return render(request,'testapp/results.html')