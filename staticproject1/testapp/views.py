from django.shortcuts import render
import datetime
# Create your views here.
def static_view(request):
    date = datetime.datetime.now()
    hour = date.hour
    msg = "Hello user!!!Very "
    if hour < 12:
        msg += "Good Morning"
    elif hour < 16:
        msg += "Good Afternoon"
    elif hour < 21:
        msg += "Good Evening"
    else:
        msg += "Good Night"
    return render(request,"testapp/results.html",{"date":date,"msg":msg})