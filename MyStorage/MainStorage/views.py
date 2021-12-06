from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as django_logout

from MyStorage import settings
from .forms import *
from .models import *
from .utils import *


# Create your views here.
def storage(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    all_files = SaveFile.objects.all()
    return render(request, 'MainStorage/UserPanel.html', {'allFiles': all_files})


def addFile(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    if request.method == 'POST':
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('storage')
        else:
            print(form.errors)
    else:
        form = AddFileForm()

    return render(request, 'MainStorage/addfile.html', {'form': form})

def delFile(request, id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

    try:
        file = SaveFile.objects.get(pk=id)
        file.delete()
        return redirect("storage")
    except SaveFile.DoesNotExist:
        return HttpResponseNotFound("<h2>File not found</h2>")


def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('storage')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'MainStorage/OnlyReg.html', {'form': form})


def loginUser(request):
    if request.method == 'POST':
        user_username = request.POST['username']
        user_password = request.POST['password']
        user = authenticate(request, username=user_username, password=user_password)
        if user is not None:
            login(request, user)
            return redirect('storage')
        else:
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'MainStorage/OnlyLogin.html', {'form': form})

def logout(request):
    django_logout(request)
    return redirect('home')






