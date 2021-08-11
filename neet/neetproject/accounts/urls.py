from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]


"""
from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup, name ='signup'),
    path('login/', views.login, name ='login'),
    path('logout/', views.logout, name ='logout'),
]
"""
