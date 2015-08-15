from django.conf.urls import url
from core.views import HackList, HackCreate
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', login_required(HackList.as_view()), name='hack_list'),
    url(r'^new/?$', login_required(HackCreate.as_view()), name='hack_new'),
    url(r'^run/(?P<project>\w+)/?$', 'core.views.index', name='hackaton')
]