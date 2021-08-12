from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
"""
from django.contrib.auth.models import User
from django.contrib import auth
"""

# Create your views here.
def login_view (request) :
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(
                request=request, username=username, password=password)
            if user is not None:
                login(request, user)

        return redirect("home")
    else:
        form = AuthenticationForm()
        return render (request, 'login.html', {'form':form})


def logout_view (request) :
    logout(request)
    return redirect("home")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
        return redirect("home")
    else:
        form = RegisterForm()
        return render(request,'signup.html',{'form':form})
 





"""
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user( username=request.POST['username'], password = request.POST['password1'],
            nickname = request.POST['nickname'], email = request.POST['email'], school = request.POST['school'], major = request.POST['major'])
            auth.login(request, user)
            return redirect('home')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                return render(request, 'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('home')
    return render(request,'login.html')

 """   
