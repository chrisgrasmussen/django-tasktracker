from django.shortcuts import render, redirect
from task.forms import TaskForm, CreateUserForm, LoginForm
from task.models import Task
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    tasks = Task.objects.all()
    
    context = {'form': form, 'tasks': tasks}
    return render(request, 'task/home.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    context = {'form': form, 'task': task}
    return render(request, 'task/single-task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('home')

def registerView(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    context = {'form': form}
    return render(request, 'task/register.html', context)

def loginView(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('home') 
    
    context = {'loginform': form}    
    return render(request, 'task/login.html', context)

def logoutView(request):
    auth.logout(request)
    return redirect('login')
