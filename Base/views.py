from django.shortcuts import render
from django.views import generic
from formtools.wizard.views import SessionWizardView
from Doctores.forms import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from Doctores.models import *

# Modelo del Doctor

# Create your views here.
class TelemedicinaIndex(generic.TemplateView):
    template_name = 'base/index.html'


class Especialidades(generic.ListView):
    paginate_by = 4
    model = EspecialidadesModels
    template_name = 'base/especialidades.html'


class ListEspecialistas(generic.ListView):
    model = EspecialidadesModels
    context_object_name = 'especialistas'
    template_name = 'base/list-especialistas.html'

    def get_queryset(self):
        return DoctorModels.objects.filter(especialidad__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidad'] = EspecialidadesModels.objects.get(slug=self.kwargs['slug'])
        return context


# Define a temporary file storage location
temp_storage = FileSystemStorage(location=f'{settings.MEDIA_ROOT}/temp')

class DoctorMultiStepForm(SessionWizardView):
    form_list = [DoctorFormStep1, DoctorFormStep2]
    template_name = "base/form-registro-medico-01.html"
    file_storage = temp_storage  # Add file_storage attribute for file uploads

    def done(self, form_list, **kwargs):
        data = {}
        for form in form_list:
            data.update(form.cleaned_data)

        # Handle file fields (if any)
        if 'profile_picture' in data: 
            uploaded_file = data.pop('profile_picture')
            data['profile_picture'] = uploaded_file

        # Save the doctor model
        DoctorModels.objects.create(**data)

        return render(self.request, 'base/confirmacion-registro-doctor.html', {'data': data})

class Index2View(generic.TemplateView):
    template_name = 'base/index2.html'  

class Index3View(generic.TemplateView):
    template_name = 'base/index3.html'

