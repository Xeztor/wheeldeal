from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from wheeldeal.wheeldeal_auth.forms import SignInForm, SignUpForm


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/register.html', context)


def login_user(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignInForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')
