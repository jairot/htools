from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from django.views.generic import ListView
from core.models import Hackaton
from datetime import datetime


def index(request):
    "Simple Render"
    return render_to_response("index.html", locals(),
                              context_instance=RequestContext(request))


def tleft(request):
    "return time left to finish"
    hack = Hackaton.object.get(user=request.user)
    delta = 0
    if hack.hora_inicio < hack.hora_fin:
        delta = int(((datetime.now() - hack.hora_inicio).total_seconds())*60)
    return JsonResponse(delta, safe=False)


class HackList(ListView):
    model = Hackaton
    template_name = ''
    context_object_name = "hack_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Hackaton.objects.filter(user_id=self.user.id)

