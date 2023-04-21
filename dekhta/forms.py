from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Poets
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(max_length = 25)
    last_name = forms.CharField(max_length = 25)
    email = forms.EmailField()
    pfp = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'pfp', 'password1', 'password2']
