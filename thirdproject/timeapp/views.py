from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def time_info_view(request):
    date = datetime.datetime.now()
    response = '<h1>the current time and date now:'+str(date)+'</h1>'
    return HttpResponse(response)
