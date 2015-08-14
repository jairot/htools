import requests

from django.http import JsonResponse


def projects(request, project):
    url = "https://hackdash.org/api/v2/%s/projects" % project
    resp = requests.get(url)
    data = resp.json()
    return JsonResponse(data, safe=False)
