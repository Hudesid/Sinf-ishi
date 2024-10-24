from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task:dashboard')

        else:
            return HttpResponse('Form is invalid')

    ctx = {'form': RegisterForm}
    return render(request, 'register.html', ctx)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return redirect('task:dashboard')

            else:
                return HttpResponse('<h1 style="text-align: center;">Form is invalid</h1>')

    ctx = {'form': LoginForm}
    return render(request, 'login.html', ctx)

