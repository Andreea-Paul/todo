from django import forms
from .models import Todo

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'completed']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)     

