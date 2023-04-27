from django.shortcuts import render, redirect

from users.forms import LoginForm, RegisterForm

from django.contrib.auth.models import User

def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {
        "form": form
    })

def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            if form['password_1'].value() != form['password_2'].value():
                return redirect('register')
            
            name = form['register_name'].value()
            email = form['email'].value()
            password = form['password_1'].value()
            
            if User.objects.filter(username=name).exists():
                return redirect('register')
            
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            user.save()
            
            return redirect('login')
    
    return render(request, 'users/register.html', {
        "form": form
    })