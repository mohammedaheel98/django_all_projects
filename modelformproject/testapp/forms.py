from django import forms
from testapp.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'