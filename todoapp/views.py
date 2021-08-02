from .models import Todo
from .forms import LoginForm, TodoForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/')
def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

@login_required(login_url='/')
def add_task(request):
    todo_form = TodoForm()
    if request.method == 'POST':
        todo_form = TodoForm(request.POST or None)
        if todo_form.is_valid():
            obj = todo_form.save(commit=False)
            obj.user = request.user
            todo_form.save()
            messages.success(request, ('Task has been added!'))
            return redirect('home')
        else:
            messages.success(request, ('You must choose a date from today forward!'))

    return render(request, 'add_task.html', {'todo_form': todo_form})
            
            
@login_required(login_url='/')
def delete_task(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.delete()
    messages.success(request, ('Task has been deleted!'))
    return redirect('home')      

@login_required(login_url='/')
def mark_complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    messages.success(request, ('Task has marked as done!'))
    return redirect('home')

@login_required(login_url='/')
def mark_incomplete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    messages.success(request, ('Task has been marked as incomplete!'))
    return redirect('home')

@login_required(login_url='/')
def edit_task(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo_form = TodoForm(instance=todo)
    if request.method == 'POST':
       todo_form = TodoForm(request.POST or None, instance=todo)
       if todo_form.is_valid():
            todo_form.save()
            messages.success(request, ('Task has been edited!'))
            return redirect('home')
    return render(request, 'edit.html', {'todo_form':todo_form})      

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
                messages.info(request, "You are loged-in")
                return redirect('home')
            else:
                messages.error(request, "The username/password is wrong")
    form = LoginForm()
    return render(request, "login_page.html", {"form": form})  

def logout_view(request):
    logout(request)
    return redirect('/')          

@login_required(login_url='/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Your old password/confirm new password is incorrect')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })    

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You registered succesfully!')
            return redirect('home')
        else:    
            messages.error(request, "Your password doesn't meet the requierments/ the confirm password doesn't match/ username already used!")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})