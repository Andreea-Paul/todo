from django import forms
from django.forms import widgets
from django.forms.fields import TimeField
from .models import Todo



class DateImput(forms.DateInput):
    input_type = "date"

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

