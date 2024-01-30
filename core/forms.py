from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class_style = 'form-control'

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Twoja nazwa użytkownika',
        'class': class_style
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': class_style
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Podaj hasło',
        'class': class_style
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Powtórz hasło',
        'class': class_style
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Podaj swój login',
        'class': class_style
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Podaj hasło',
        'class': class_style
    }))

class ProfileDataForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Twoja nazwa użytkownika',
        'class': class_style
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Twój email',
        'class': class_style
    }))
    
class ProfilePasswordForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Podaj hasło',
        'class': class_style
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Powtórz hasło',
        'class': class_style
    }))

    