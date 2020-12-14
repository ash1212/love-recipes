from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserLoginForm, RegisterForm
from django.contrib.auth import get_user_model
User = get_user_model()


def registerView(request, *args, **kwargs):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        login(request, new_user)
        return HttpResponseRedirect('/accounts/thanks/')
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {'form': form})


def loginView(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect('/my-recipes/')
    return render(request, "accounts/login.html", {"form": form})


def logoutView(request):
    logout(request)
    return HttpResponseRedirect("/")
