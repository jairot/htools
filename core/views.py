from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from core.models import Hackaton


def index(request, project):

    return render_to_response("index.html", context={'project': project},
                              context_instance=RequestContext(request))


class HackList(ListView):
    model = Hackaton
    template_name = ''
    context_object_name = "hack_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(HackList, self).get_context_data(**kwargs)
        context['project'] = self.kwargs['project']
        return context

    def get_queryset(self):
        return Hackaton.objects.filter(user_id=self.user.id)

