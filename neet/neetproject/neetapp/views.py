from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import TeamForm
from .models import Team

# Create your views here.
def competition (request):
    return render (request, "competition.html")

def home_loginO (request):
    return render (request, "home_loginO.html")

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

def recruitmentlist (request):
    teams = Team.objects.all()
    return render (request, "recruitmentlist.html", {'teams':teams})

def detailpage (request, id):
    team = get_object_or_404(Team, pk=id)
    return render(request, "detailpage.html", {'team':team})

def recruitment (request):
    form = TeamForm()
    return render (request, "recruitment.html", {'form':form})

def teams_create(request):
    form = TeamForm(request.POST)
    if form.is_valid:
        new_team = form.save(commit=False)
        new_team.pub_date = timezone.now()
        new_team.save()
        return redirect('detailpage',new_team.id)
    return redirect('home')

def teams_edit(request,id):
    edit_team = Team.objects.get(id=id)
    return render(request, 'teams_edit.html', {'team':edit_team})

def teams_update(request,id):
    update_team = Team.objects.get(id=id)
    update_team.title = request.POST['title']
    update_team.body = request.POST['body']
    update_team.writer = request.POST['writer']
    update_team.pub_date = timezone.now()
    update_team.num = request.POST['num']
    update_team.save()
    return redirect('detailpage', update_team.id)

def teams_delete(request,id):
    delete_team = Team.objects.get(id=id)
    delete_team.delete()
    return redirect('recruitmentlist')

def review (request):
    return render (request, "review.html")

def signup (request):
    return render (request, "signup.html")

def message (request):
    return render(request, "message.html")