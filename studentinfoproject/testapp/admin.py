from django.contrib import admin
from testapp.models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('rollno','name','dob','email','mark','phoneno','address')

