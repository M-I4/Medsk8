from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request:HttpRequest):
    return render(request , "skateboardBlog/home.html")



def list_posts(request: HttpRequest):
    if "search" in request.GET:
        posts = Post.objects.filter(title__contains=request.GET["search"])
    else:
        posts = Post.objects.all()

    
    #posts = Post.objects.all().order_by("-publish_date") #to order by date
    #posts = Post.objects.filter(is_published=False) #to filter by exact
    #posts = Post.objects.filter(title__contains = "aims") #to filter using postfix __contains
    return render(request, "skateboardBlog/view_posts.html", {"posts" : posts})


@login_required(login_url="/accounts/login")
def add_post(request : HttpRequest):
  
    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content = request.POST["content"], publish_date=request.POST["publish_date"], post_type=request.POST["post_type"] , image=request.FILES["image"])
        new_post.save()
        return render(request , "skateboardBlog/add_post.html")
    return render(request , "skateboardBlog/add_post.html", {"Post" : Post})

def register(request:HttpRequest):
    return render(request, "accounts/register.html")


def login(request:HttpRequest):
    return render(request, "accounts/login.html")


