from django.conf.urls import url
from timer.views import TimerTemplate

urlpatterns = [
    url(r'^$', TimerTemplate.as_view(), name='timer_template'),
    url(r'^timeleft/(?P<project>\w+)/?$', 'timer.views.tleft', name='tleft'),
]
