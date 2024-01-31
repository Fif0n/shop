from django import forms

from .models import OrderUserData

class_style = 'form-control'

class OrderUserDataForm(forms.ModelForm):
    class Meta:
        model = OrderUserData
        fields = ('description', 'name', 'address')
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Dodatkowe informacje o zamówieniu',
                'class': class_style
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Imię i nazwisko',
                'class': class_style
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Adres',
                'class': class_style
            })
        }
    