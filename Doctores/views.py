from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *

from django.urls import reverse_lazy

# Create your views here.
class DoctorIndex(generic.ListView):
    model = DoctorModels
    context_object_name = 'doctores'
    template_name = 'doctores/index-doctores.html'

class DoctorNew(generic.CreateView):
    model = DoctorModels
    form_class = DoctorForms
    template_name = 'doctores/forms-doctores.html'
    success_url = reverse_lazy('doctores:doctores')

class DoctorEdit(generic.UpdateView):
    model = DoctorModels
    form_class = DoctorForms
    template_name = 'doctores/forms-doctores.html'
    success_url = reverse_lazy('doctores:doctores')


