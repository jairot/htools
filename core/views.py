from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse


def index(request):

    return render_to_response("index.html", locals(),
                              context_instance=RequestContext(request))


def tleft(request):

    t = {}
    return JsonResponse(t, safe=False)
