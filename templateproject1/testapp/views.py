from django.shortcuts import render
import datetime
# Create your views here.
def template_view(request):
    dt = datetime.datetime.now()
    my_dict = {'date':dt,'name':'mohammed aheel','age':23,'city':'karaikudi'}
    return render(request,'testapp/results.html',my_dict)