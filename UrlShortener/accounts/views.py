from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, authenticate, logout
from urlshort.models import Url


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        print(form.errors)
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render(request=request, template_name='accounts/register.html', context={'register_form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Вы зарегестрированы как {username}.")
                return redirect('/')
            else:
                messages.error(request, "Неверно введен логин или пароль.")
        else:
            messages.error(request, "Неверно введен логин или пароль.")
    form = AuthenticationForm()
    return render(request=request, template_name='accounts/login.html', context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, 'logged out')
    return redirect('/')


def profile(request):
    user = User.objects.get(username=request.user)
    token = Url.objects.filter(user=user).order_by('-created_at')
    return render(request, 'accounts/profile.html', {'token': token})

