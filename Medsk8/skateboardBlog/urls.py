from django.urls import path
from . import views

app_name = "skateboardBlog"

urlpatterns = [
    path('', views.home, name = "home"),
    path('add/post/', views.add_post, name = "add_post"),
    path('view/post/', views.list_posts, name = "list_post"),
    
] 
