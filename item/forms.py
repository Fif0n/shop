from django import forms
from .models import Opinion

class_style = 'form-control'

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ('rating', 'content')
        widgets = {
            'rating': forms.TextInput(attrs={
                'value': 5,
                'class': class_style,
                'type': 'number'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Twoja opinia',
                'class': class_style
            })
        }
