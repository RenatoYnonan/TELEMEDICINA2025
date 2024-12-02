from django.urls import path
from .views import *

urlpatterns = [
    path('panel-general', PanelControlIndex.as_view(), name='panel-general')
]