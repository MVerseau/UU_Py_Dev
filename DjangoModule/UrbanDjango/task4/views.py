from django.shortcuts import render
from django.views.generic import TemplateView


class MainPageTemplate(TemplateView):
    template_name = r'fourth_task\index.html'

def catalogtemplate(request):
    template_name = r'fourth_task\catalog.html'
    context = {
        'title': 'Catalog',
        'items':['tank_top','hoody','smth else']
    }
    return render(request, template_name, context)


class CartTemplate(TemplateView):
    template_name = r'fourth_task\cart.html'
