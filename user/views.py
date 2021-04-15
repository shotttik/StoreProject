from django.contrib import auth
from django.shortcuts import render, redirect

from user.forms import UserCreationForm


def signup(request):
    registration_form = UserCreationForm()
    if request.method == 'POST':
        registration_form = UserCreationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('login')
    return render(request, 'user/user_signup.html', {'form': registration_form})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'], password=request.POST['password'],)
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            return render(request, 'user/user_login.html', {'error': 'Email or password is incorrect'})

    return render(request, 'user/user_login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')
