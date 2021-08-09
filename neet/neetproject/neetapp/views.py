from django.shortcuts import render

# Create your views here.
def competition (request):
    return render (request, "competition.html")

def detailpage (request):
    return render (request, "detailpage.html")


def home (request):
    return render (request, "home.html")

def login (request):
    return render (request, "login.html")

def members (request):
    return render (request, "members.html")

def myteam (request):
    return render (request, "myteam.html")

def portfolioh (request):
    return render (request, "portfolioh.html")

def profile (request):
    return render (request, "profile.html")

def recruitment (request):
    return render (request, "recruitment.html")

def recruitmentlist (request):
    return render (request, "recruitmentlist.html")

def review (request):
    return render (request, "review.html")

def signup (request):
    return render (request, "signup.html")

def message (request):
    return render(request, "message.html")