from django import forms
from .models import *

class DoctorForms(forms.ModelForm):
    class Meta:
        model = DoctorModels
        fields = ['picture', 'nombre_completo', 'apellido','tipo_documento',
                   'numero_documento','Genero','especialidad',
                   'cmp', 'experiencia','ciudad', 'edad',
                    'telefono', 'correo_electronico', 'estado']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'numero_documento': forms.NumberInput(attrs={'class': 'form-control'}),
            'Genero': forms.Select(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}),
            'cmp': forms.TextInput(attrs={'class': 'form-control'}),
            'experiencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class DoctorFormStep1(forms.ModelForm):
    class Meta:
        model = DoctorModels
        fields = ['picture', 'nombre_completo',  'apellido', 'tipo_documento',
                'numero_documento','Genero', 'especialidad','cmp']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'numero_documento': forms.NumberInput(attrs={'class': 'form-control'}),
            'Genero': forms.Select(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}),
            'cmp': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DoctorFormStep2(forms.ModelForm):
    class Meta:
        model = DoctorModels
        fields = ['experiencia','ciudad', 'edad',
                'telefono', 'correo_electronico', ]
        
        widgest = {
            'experiencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
        }