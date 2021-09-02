from django.contrib import admin
from testapp.models import Beer 
# Register your models here.
@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ['name','taste','color','price']
