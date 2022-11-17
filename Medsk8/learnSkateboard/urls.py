from django.urls import path
from . import views


app_name = "learnSkateboard"


urlpatterns = [
    path('', views.home, name = "home"),
    path('components/', views.components, name = "components"),
    
] 



