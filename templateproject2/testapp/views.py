from django.shortcuts import render
import datetime
# Create your views here.
def greeting_info(request):
    dt = datetime.datetime.now()
    hour = dt.hour
    msg = 'Hello User!!!!Very Veryy '
    if hour < 12:
        msg = msg + 'Good Morning'
    elif hour < 16:
        msg = msg + 'Good Afternoon'
    elif hour < 21:
        msg = msg +'Good Evening'
    else:
        msg = msg + 'Good Night'
    return render(request,'testapp/results.html',{'date':dt,'msg':msg})