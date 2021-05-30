from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('/home',views.home,name='home')
]
