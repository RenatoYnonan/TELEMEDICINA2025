from django.urls import path
from .views import *

urlpatterns = [
    path('doctores', DoctorIndex.as_view(), name='doctores'),
    path('new-doctores', DoctorNew.as_view(), name='new-doctores'),
    path('edit-doctores/<int:pk>', DoctorEdit.as_view(), name='edit-doctores'),

    #Especialidades
    
]