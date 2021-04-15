from django.contrib import auth
from django.shortcuts import render, redirect

from user.forms import UserCreationForm
from user.models import User


def signup(request):
    registration_form = UserCreationForm()
    if request.method == 'POST':
        try:
            User.objects.get(personal_number=request.POST['personal_number'])
        except User.DoesNotExist:
            registration_form = UserCreationForm(request.POST)
            if registration_form.is_valid():
                user: User = registration_form.save(commit=False)
                user.save()
                return redirect('login')
    return render(request, 'user/user_signup.html', {'form': registration_form})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'], password=request.POST['password'],)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'user/user_login.html', {'error': 'Email or password is incorrect'})

    return render(request, 'user/user_login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')
