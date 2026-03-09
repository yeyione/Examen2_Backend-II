from django import forms
from .models import Auto


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'año', 'precio']
        widgets = {
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Toyota'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Corolla'
            }),
            'año': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 2023',
                'min': 1900,
                'max': 2100
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 250000.00',
                'step': '0.01'
            }),
        }
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'año': 'Año',
            'precio': 'Precio ($)',
        }
