from django.shortcuts import render
from django.views import generic
# Create your views here.
class PacientesIndex(generic.TemplateView):
    template_name = 'pacientes/index-pacientes.html'
