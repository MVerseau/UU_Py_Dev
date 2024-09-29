from django.shortcuts import render
from django.views.generic import TemplateView


class MainPageTemplate(TemplateView):
    template_name = r'third_task\index.html'


def catalogtemplate(request):
    template_name = r'third_task\catalog.html'
    context = {
        'title': 'Catalog',
        'item1':'tank_top',
        'item2': 'hoody',
        'item3':'smth else',
    }
    return render(request, template_name, context)


class CartTemplate(TemplateView):
    template_name = r'third_task\cart.html'
