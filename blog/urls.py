from django import views
from django.contrib import admin
from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path('', blog_views.index, name="Shop Home"),
]