from django.contrib import admin
from testapp.models import Company
# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','location','ceo']