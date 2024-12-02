from django.shortcuts import render
from django.views import generic


# Create your views here.
class PanelControlIndex(generic.TemplateView):
    template_name = 'panel-control/index.html'