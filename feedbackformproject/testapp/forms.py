from django import forms
from django.core import validators
from django.forms.widgets import PasswordInput
class FeedBackForm(forms.Form):
    Name = forms.CharField()
    Rollno = forms.IntegerField()
    Email = forms.EmailField()
    password = forms.CharField(label="Password",widget=PasswordInput,validators=[validators.MinLengthValidator(8),validators.RegexValidator(regex="^[a-zA-Z0-9]*$",message="password must be alphanumeric",code="invalid password")])
    rpassword = forms.CharField(label="Confirm Password",widget=PasswordInput,validators=[validators.MinLengthValidator(8)])
    Feedback = forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(20),validators.MinLengthValidator(10)])
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        total_cleaned_data = super().clean()
        pswd = total_cleaned_data["password"]
        rpswd = total_cleaned_data["rpassword"]
        if pswd != rpswd:
            raise forms.ValidationError("password must be same")
        inputrollno = total_cleaned_data["Rollno"]
        if inputrollno <= 0:
            raise forms.ValidationError("Roll no should not be 0")
        inputemail = total_cleaned_data["Email"]
        if inputemail[-9:] != "gmail.com":
            raise forms.ValidationError("Email must be gmail only")
        bot_handler_value = total_cleaned_data["bot_handler"]
        if len(bot_handler_value) > 0:
            raise forms.ValidationError("The request is from BOT,form not submitted")











'''# this method is not recommeded
    def clean_Rollno(self):
        inputrollno = self.cleaned_data["Rollno"]
        if inputrollno <= 0:
            raise forms.ValidationError("Roll not be 0")
        return inputrollno
    def clean_Name(self):
        inputname = self.cleaned_data["Name"]
        if inputname[0].lower() != "a":
            raise forms.ValidationError("name should be start with A")
        return inputname
'''

