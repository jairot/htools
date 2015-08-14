from django.conf.urls import include, url
from timer.views import TimerTemplate

urlpatterns = [
    url(r'^$', TimerTemplate.as_view(), name='timer_template'),
]
