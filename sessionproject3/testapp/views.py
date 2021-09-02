from django.shortcuts import render
from testapp.forms import *

# Create your views here.
def add_item_view(request):
    form = AddItemForm()
    if request.method == 'POST':
        name = request.POST["name"]
        quantity = request.POST["quantity"]
        request.session[name]=quantity
        request.session.set_expiry(120)
    return render(request,'testapp/home.html',{"form":form})

def cart_view(request):
    return render(request,"testapp/cart.html")