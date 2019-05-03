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
    error=False
    if request.method == 'POST':
        book_tag = request.POST.get("select_tag")
        book_name = request.POST.get("book_name")
        book_author = request.POST.get("book_author")
        book_year = request.POST.get("book_year")
        book_rank = request.POST.get("book_rank")
        book_cost0 = request.POST.get("book_cost0")
        book_cost1 = request.POST.get("book_cost1")
        if request.POST.get("book_description") is not None:
            book_description = request.POST.get("book_description")
        newpost = post(name=book_name , author=book_author , year=book_year , rank=book_rank , old_price=book_cost0 , new_price=book_cost1 , description=book_description , tag=book_tag)
        newpost.save()
        if newpost is not None:
            error=True
    return render(request, "createpost.html",{
    "error" : error
    })
