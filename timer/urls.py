from django.conf.urls import url

urlpatterns = [
    url(r'^timeleft/(?P<project>\w+)/?$', 'timer.views.tleft', name='tleft'),
]
