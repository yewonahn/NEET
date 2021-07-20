from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def hello(request):
    userName=request.GET['name']
    return render(request,"hello.html",{'userName':userName})
    