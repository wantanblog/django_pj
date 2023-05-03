from django.contrib import admin
from django.urls import path
from form_app import views

urlpatterns = [
    path('home', views.index,name='index'),
    path('', views.index,name='index'),
    path('entryInit', views.entryInit,name='entryInit'),
    path('entry', views.entry,name='entry'),
    path('refer', views.refer,name='refer'),
    path('search', views.search,name='search'),
    path('edit/<int:num>', views.edit,name='edit'),
    path('editInit/<int:num>', views.editInit,name='editInit'),
    path('delete/<int:num>', views.delete,name='delete'),
]