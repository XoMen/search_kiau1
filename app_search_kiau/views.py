from django.shortcuts import render, HttpResponseRedirect,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from app_search_kiau.models import *


def home(request):
    mypost = post.objects.all().order_by('-id')

    return render(request, "home.html",{
    "mypost":mypost,
    })


def login_(request):
    error = False
    error2 = False
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        elif User.objects.filter(username=username).exists() == False:
            error2=True
        elif user is None:
            error=True
    return render(request, "login.html",{
    "error":error,
    "error2":error2
    })
def logout_(request):
        logout(request)
        return HttpResponseRedirect("/")

def createpost(request):
    return render(request,"createpost.html")        
