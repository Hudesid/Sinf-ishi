from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, Task


@login_required
def logout_view(request):
    logout(request)
    return redirect('user:login')

@login_required
def dashboard_view(request):
    tasks = Task.objects.all()

    ctx = {'tasks': tasks}
    return render(request, 'dashboard.html', ctx)

@login_required
def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task:dashboard')

    return render(request, 'confirm.html', {'task': task})

@login_required
def update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:dashboard')

        else:
            return HttpResponse('<h1 style="text-align: center;">Form is invalid</h1>')
    up = 'up'
    ctx = {'form': TaskForm(instance=task), 'up':up}
    return render(request, 'create-task.html', ctx)

@login_required
def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task:dashboard')

        else:
            return HttpResponse('<h1 style="text-align: center;">Form is invalid</h1>')

    ctx = {'form': TaskForm}
    return render(request, 'create-task.html', ctx)