"""neetproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
import neetapp.views
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('competition/',neetapp.views.competition, name="competition"),
    path('detailpage/',neetapp.views.detailpage, name="detailpage"),
    path('home/',neetapp.views.home, name="home"),
    path('members/',neetapp.views.members, name="members"),
    path('members_detail/<str:id>',neetapp.views.members_detail, name="members_detail"),
    path('members_new/',neetapp.views.members_new, name="members_new"),
    path('members_create/',neetapp.views.members_create, name="members_create"),
    path('members_edit/<str:id>',neetapp.views.members_edit, name="members_edit"),
    path('members_update/<str:id>',neetapp.views.members_update, name="members_update"),
    path('members_delete/<str:id>',neetapp.views.members_delete, name="members_delete"),
    path('myteam/',neetapp.views.myteam, name="myteam"),
    path('portfolioh/',neetapp.views.portfolioh, name="portfolioh"),
    path('profile/',neetapp.views.profile, name="profile"),
    path('recruitment/',neetapp.views.recruitment, name="recruitment"),
    path('recruitmentlist/',neetapp.views.recruitmentlist, name="recruitmentlist"),
    path('review/',neetapp.views.review, name="review"),
    path('message/',neetapp.views.message,name="message"),
    path('', neetapp.views.home, name="home"),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)