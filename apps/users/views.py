from django.shortcuts import render, redirect

from apps.users.forms import LoginForm, RegisterForm

from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            name = form['login_name'].value()
            password = form['password'].value()
            
        user = auth.authenticate(
            request,
            username=name,
            password=password,
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{name} logged successfully!')
            return redirect('index')
        else:
            messages.error(request, "Error when logging in")
            return redirect('login')
        
    
    return render(request, 'users/login.html', {
        "form": form
    })

def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            name = form['register_name'].value()
            email = form['email'].value()
            password = form['password_1'].value()
            
            if User.objects.filter(username=name).exists():
                messages.error(request, "User already exists!")
                return redirect('register')
            
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            user.save()
            
            messages.success(request, 'Registration successful!')
            return redirect('login')
    
    return render(request, 'users/register.html', {
        "form": form
    })
    
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')
    