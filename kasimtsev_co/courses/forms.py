from django.forms import ModelForm
from django import forms
from . import models


class UserQuestionsForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'Имя',
        } 
    ))
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$',widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Телефон',
        } ))
    class Meta:
        model = models.AnonymusQuestion
        fields = ['name', 'phone']
