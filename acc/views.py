from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User

# Create your views here.
def index(request):
    return render(request, "acc/index.html")
    
def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        user = authenticate(username=un, password=up)

        if user:
            login(request, user)
            return redirect("acc:index")
        else:
            pass
    return render(request, "acc/login.html")

def userlogout(request):
    logout(request)
    return redirect("acc:index")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        p = request.FILES.get("upic")
        com = request.POST.get("ucom")

        try:
            User.objects.create_user(username=un, password=up, pic=p, comment=com)
            return redirect("acc:login")
        except:
            pass
    return render(request, "acc/signup.html")

def profile(request):
    return render(request, "acc/profile.html")

def update(request):
    if request.method == "POST":
        user = request.user
        ue = request.POST.get("umail")
        up = request.FILES.get('upic')
        uc = request.POST.get("ucom")

        user.email, user.pic, user.comment = ue, up, uc
        user.save()
        login(request, user)
        return redirect("acc:profile")
    return render(request, "acc/update.html")