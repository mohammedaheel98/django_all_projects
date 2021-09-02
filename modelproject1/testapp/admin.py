from django.contrib import admin
from django.contrib.admin.decorators import register
from testapp.models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','eno','enname','esal','eaddr')
    ordering = ('enname',)
    search_fields = ('ename','eaddr',)

#admin.site.register(Employee)
