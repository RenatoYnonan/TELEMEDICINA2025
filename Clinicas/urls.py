from django.urls import path
from  .views import *

urlpatterns = [
    path('clinicas', ClinicasIndex.as_view(), name='clinicas'),
]