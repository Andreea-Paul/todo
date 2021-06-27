from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            todos = Todo.objects.all()
            messages.success(request, ('Task has been added!'))
            return render(request, 'home.html', {'todos': todos})
    else:
        todos = Todo.objects.all()
        return render(request, 'home.html', {'todos': todos})