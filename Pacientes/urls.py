from django.urls import path
from .views import *

urlpatterns = [
    path('pacientes', PacientesIndex.as_view(), name='pacientes'),
]