from django.shortcuts import render
from django.views.generic import TemplateView

def func_view(request):
    return render(request,r'second_task\func.html')


class ClassView(TemplateView):
    template_name = r'second_task\class.html'