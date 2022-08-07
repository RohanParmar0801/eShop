from django import views
from django.contrib import admin
from django.urls import path
from shop import views as shop_views

urlpatterns = [
    path('', shop_views.index, name="Shop Home"),
]