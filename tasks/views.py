from django.shortcuts import render,redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
# Create your views here.
def home(req):
    tasks=Task.objects.filter(user=req.user)
    return render(req,"tasks/home.html",{'tasks':tasks})

@login_required
def add_task(req):
    if req.method=="POST":
        form=TaskForm(req.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = req.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(req, 'tasks/add_task.html', {'form': form})