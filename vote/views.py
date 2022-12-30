from django.shortcuts import render, redirect
from vote.models import Topic, Choice

# Create your views here.
def index(request):
    if request.user.is_anonymous:  # 인증된 사용자만 vote페이지 들어갈 수 있도록.
        return redirect("acc:login")
    t = Topic.objects.all()
    context = {
        "tset" : t
    }
    return render(request, "vote/index.html", context)

def detail(request, vpk):
    t = Topic.objects.get(id=vpk)
    c = t.choice_set.all()
    context = {
        "t" : t,
        "cset" : c
    }
    return render(request, "vote/detail.html", context)

def vote(request, vpk):
    t = Topic.objects.get(id=vpk)

    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk = request.POST.get("cho")
        c = Choice.objects.get(id=cpk)
        c.choicer.add(request.user)
    return redirect("vote:detail", vpk)

def cancel(request, vpk):
    u = request.user
    t = Topic.objects.get(id=vpk)
    t.voter.remove(u)
    u.choice_set.get(top=t).choicer.remove(u)
    return redirect("vote:detail", vpk)

def create(request):
    if request.method == "POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        ch = request.POST.getlist("cho")
        chc = request.POST.getlist("chocom")

        t = Topic(subject=s, maker=request.user, content=c)
        t.save()

        return redirect("vote:index")
    return render(request, "vote/create.html")