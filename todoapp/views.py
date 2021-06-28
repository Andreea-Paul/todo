from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import Todo
from .forms import LoginForm, TodoForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
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

@login_required(login_url='/')
def delete_task(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, ('Task has been Deleted!'))
    return redirect('home')      

@login_required(login_url='/')
def mark_complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('home')

@login_required(login_url='/')
def mark_incomplete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('home')

@login_required(login_url='/')
def edit_task(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        form = TodoForm(request.POST or None, instance=todo)

        if form.is_valid():
            form.save()
            messages.success(request, ('Task has been edited!'))
            return redirect('home')
    else:
        todo = Todo.objects.get(id=todo_id)
        return render(request, 'edit.html', {'todo': todo})    

def login_view(request):
    error_message = None
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, "User loged-in")
                return redirect('home')
            else:
                messages.error(request, "Username/password is wrong")
    form = LoginForm()
    return render(request, "login_page.html", {"form": form})  

def logout_view(request):
    logout(request)
    return redirect('/')          