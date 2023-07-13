from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms



class UserSignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'Имя',
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'Фамилия',
        }
    ))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Почта',
        }
    ))

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'input', 
               'placeholder': 'Логин'}
    ))


    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input',
            'placeholder': 'Пароль',
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input',
            'placeholder': 'Повторите пароль',
        }
    ))

    class Meta:
        model = User
        fields = ( "first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input',
            'placeholder': 'Пароль',
        }
    ))
