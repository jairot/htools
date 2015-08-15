from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from core.models import Hackaton
from core.forms import HackatonForm

@login_required()
def index(request, project):
    project = Hackaton.objects.get(pk=project)
    return render_to_response("index.html", context={'project': project},
                              context_instance=RequestContext(request))


class HackList(ListView):
    login_required = True
    model = Hackaton
    context_object_name = 'hack_list'
    template_name = "hack_list.html"
    paginate_by = 10

    def get_queryset(self):
        return self.request.user.hackatones.all()


class HackCreate(CreateView):
    login_required = True
    form_class = HackatonForm
    template_name = "hack_new.html"
    success_url = '/'

