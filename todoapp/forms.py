from django import forms
from django.forms import widgets
from django.forms.fields import TimeField
from .models import Todo
import datetime


class DateImput(forms.DateInput):
    input_type = "date"

def present_or_future_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    return value

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'completed', 'category', 'due_date']
        widgets = {
            'due_date': DateImput()
        }
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)     

