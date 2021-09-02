from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This response is from Class based views</h1>')

class HelloWorldTemplateView(TemplateView):
    template_name = 'testapp/home.html'

class ViewContext(TemplateView):
    template_name = 'testapp/context.html'
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['name'] = 'aheel'
        context['age'] = 23
        context['city'] = 'karaikudi'
        return context