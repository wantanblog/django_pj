from django.contrib import admin
from django.urls import path
from form_app import views

urlpatterns = [
    path('', views.index,name='index'),
    path('form', views.form,name='form'),
]