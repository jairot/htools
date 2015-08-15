import datetime
from django.views.generic import TemplateView
from django.http import JsonResponse

from core.models import Hackaton


class TimerTemplate(TemplateView):
    template_name = 'timer.html'


def tleft(request, project):
    "return time left to finish"
    hack = Hackaton.objects.get(pk=project)
    delta = 0
    if hack.hora_inicio < hack.hora_fin:
        delta = int(((datetime.now() - hack.hora_inicio).total_seconds())*60)
    return JsonResponse(delta, safe=False)
