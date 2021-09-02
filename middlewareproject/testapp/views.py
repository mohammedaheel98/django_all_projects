from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome_view(request):
    print('this line is processing at view')
    return HttpResponse('<h1>Custom demo middleware</h1>')