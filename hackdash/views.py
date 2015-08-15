import requests

from django.http import JsonResponse


def projects(request, project):
    """
    {
        "_id": String
      , "title": String
      , "domain": String
      , "description": String
      , "leader": User
      , "status": String
      , "contributors": [User]
      , "followers": [User]
      , "cover": String
      , "link": String
      , "tags": [String]
      , "active": Boolean
      , "created_at": Date
    }
    """
    url = "https://hackdash.org/api/v2/%s/projects" % project
    resp = requests.get(url)
    data = resp.json()
    return JsonResponse(data, safe=False)
