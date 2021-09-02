from django.shortcuts import render
from . import forms
# Create your views here.
def feedback_form(request):
    if request.method == "POST":
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            print("validating student feedback...")
            print("name:",form.cleaned_data['Name'])
            print("rollno:",form.cleaned_data['Rollno'])
            print("email:",form.cleaned_data['Email'])
            print("feedback:",form.cleaned_data['Feedback'])
            
    else:
        form = forms.FeedBackForm()
    return render(request,'testapp/index.html',{"form":form})
