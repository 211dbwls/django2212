from django.urls import path
from . import views

app_name = "acc"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('update/', views.update, name="update")
]