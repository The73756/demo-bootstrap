from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from demo2app.models import Request


class RegistrationForm(UserCreationForm):
    phone = forms.CharField(label='Номер телефона')
    patronymic = forms.CharField(label='Отчество')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='Адрес электронной почты')

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'patronymic', 'phone', 'email']


class CreateRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['address', 'phone', 'date', 'type', 'payment_type', 'is_other', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'datetime-local'}),
        }
