from django.shortcuts import render
from django.views.generic import TemplateView



class TimerTemplate(TemplateView):
    template_name = 'timer.html'

