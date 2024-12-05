from django.urls import path
from .views import *

urlpatterns = [
    path('', TelemedicinaIndex.as_view(), name='telemedicina'),
    path('especialidades/', Especialidades.as_view(), name='especialidades'),
    path('list-especialidad/<slug:slug>/', ListEspecialistas.as_view(), name='list-especialidad'),

    # REGISTRO
    path('registro-especialista/', DoctorMultiStepForm.as_view(), name='registro-especialista'),

    path('index2/', Index2View.as_view(), name='index2'),
    path('index3/', Index3View.as_view(), name='index3',)

]
