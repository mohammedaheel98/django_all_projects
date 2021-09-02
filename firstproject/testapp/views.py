from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def date_time_view(request):
    date = datetime.datetime.now()
    response = '<h1>This is the current time and date now:'+str(date)+'</h1>'
    return HttpResponse(response)