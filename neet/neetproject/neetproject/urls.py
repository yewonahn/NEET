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
from django.contrib import admin
from django.urls import path
import neetapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('competition/',neetapp.views.competition, name="competition"),
    path('home_loginO/',neetapp.views.home_loginO, name="home_loginO"),
    path('home/',neetapp.views.home, name="home"),
    path('login/',neetapp.views.login, name="login"),
    path('members/',neetapp.views.members, name="members"),
    path('myteam/',neetapp.views.myteam, name="myteam"),
    path('portfolioh/',neetapp.views.portfolioh, name="portfolioh"),
    path('profile/',neetapp.views.profile, name="profile"),
    path('recruitmentlist/',neetapp.views.recruitmentlist, name="recruitmentlist"),
    path('detailpage/',neetapp.views.detailpage, name="detailpage"),
    path('recruitment/',neetapp.views.recruitment, name="recruitment"),
    path('teams_create/',neetapp.views.teams_create, name="teams_create"),
    path('teams_edit/<str:id>',neetapp.views.teams_edit, name="teams_edit"),
    path('teams_update/<str:id>',neetapp.views.teams_update, name="teams_update"),
    path('teams_delete/<str:id>',neetapp.views.teams_delete, name="teams_delete"),
    path('review/',neetapp.views.review, name="review"),
    path('signup/',neetapp.views.signup, name="signup"),
    path('message/',neetapp.views.message,name="message"),
    path('', neetapp.views.home, name="home"),
]