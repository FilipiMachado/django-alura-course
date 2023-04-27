from django.shortcuts import render

from users.forms import LoginForm

def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {
        "form": form
    })

def register(request):
    return render(request, 'users/register.html')