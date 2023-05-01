from django.contrib import admin
from django.urls import path
from form_app import views

urlpatterns = [
    path('home', views.index,name='index'),
    path('', views.index,name='index'),
    path('entry', views.entry,name='entry'),
    path('refer', views.refer,name='refer'),
    path('search', views.search,name='search'),
]