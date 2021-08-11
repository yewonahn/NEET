from .models import Member
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import MemberForm

# Create your views here.
def competition (request):
    return render (request, "competition.html")

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

def recruitment (request):
    return render (request, "recruitment.html")

def recruitmentlist (request):
    return render (request, "recruitmentlist.html")

def review (request):
    return render (request, "review.html")

def message (request):
    return render(request, "message.html")