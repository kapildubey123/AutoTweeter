from django.shortcuts import render

# Create your views here.
from django.urls import path

from . import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
]