from django.shortcuts import render
from django.views import generic

# Create your views here.
class ClinicasIndex(generic.TemplateView):
    template_name = 'clinicas/index-clinicas.html'