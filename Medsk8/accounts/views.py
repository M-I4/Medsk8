from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from skateboardBlog import urls
# Create your views here.

def register(request:HttpRequest):
    if request.method == "POST":

        new_user = User.objects.create_user(username=request.POST["email"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_profile = Profile(user = new_user, avatar = request.FILES["avatar"], city= request.POST["city"], gender = request.POST["gender"], age = request.POST["age"], is_skater = request.POST["is_skater"], phoneNumber = request.POST["phoneNumber"])
        new_user.save()
        new_profile.save()

    return render(request, 'accounts/register.html')


def login_user(request:HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        
        if user:
            login(request, user)
            return redirect("skateboardBlog:home")
        else:
            msg = "User Not Found , check your credentials"

    return render(request, "accounts/login.html", {"msg" : msg})
    

