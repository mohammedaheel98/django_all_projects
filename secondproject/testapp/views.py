from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse('<h1>First Response</h1>')

def second_view(request):
    return HttpResponse('<h1>Second Response</h1>')

def third_view(request):
    return HttpResponse('<h1>Third Response</h1>')

def fourth_view(request):
    return HttpResponse('<h1>Fourth Response</h1>')

def fifth_view(request):
    return HttpResponse('<h1>Fifth Response</h1>')
