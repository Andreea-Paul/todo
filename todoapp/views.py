from django.shortcuts import render
from .models import Todo

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})
