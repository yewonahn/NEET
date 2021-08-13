from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import TeamForm
from .models import Team
from .models import Member
from .forms import MemberForm

# Create your views here.
def competition (request):
    return render (request, "competition.html")

def home_loginO (request):
    return render (request, "home_loginO.html")
def detailpage (request):
    return render (request, "detailpage.html")

def home (request):
    return render (request, "home.html")


def members (request):
    members = Member.objects.all()
    return render (request, "members.html", {'members':members})

def members_detail(request, id):
    member = get_object_or_404(Member, pk=id)
    return render(request, 'members_detail.html', {'member':member})

def members_new(request):
    form = MemberForm()
    return render(request, 'members_new.html',{'form':form})

def members_create(request):
    form = MemberForm(request.POST, request.FILES)
    if form.is_valid:
        new_member = form.save(commit=False)
        new_member.pub_date = timezone.now()
        new_member.save()
        return redirect('members_detail',new_member.id)
    return redirect('home')
#    new_member = Member()
#    new_member.title = request.POST['title']
#    new_member.body = request.POST['body']
#    new_member.title_image = request.FILES['title_image']
#    new_member.pub_date = timezone.now()
#    new_member.save()
#    return redirect('members_detail', new_member.id)


def members_edit(request,id):
    edit_member = Member.objects.get(id=id)
    return render(request, 'members_edit.html', {'member':edit_member})

def members_update(request,id):
    update_member = Member.objects.get(id=id)
    update_member.title = request.POST['title']
    update_member.body = request.POST['body']
    update_member.pub_date = timezone.now()
    update_member.save()
    return redirect('members_detail', update_member.id)

def members_delete(request,id):
    delete_member = Member.objects.get(id=id)
    delete_member.delete()
    return redirect('members')

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

def message (request):
    return render(request, "message.html")