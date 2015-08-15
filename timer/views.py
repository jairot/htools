import datetime
from django.views.generic import TemplateView
from django.http import JsonResponse
from core.models import Hackaton


def tleft(request, project):
    "return time left to finish"
    hack = Hackaton.objects.get(pk=project)
    delta = (datetime.datetime.now() - hack.hora_inicio.utcnow()).microseconds
    return JsonResponse(delta, safe=False)
