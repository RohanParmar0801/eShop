from django import views
from django.contrib import admin
from django.urls import path
from shop import views as shop_views

urlpatterns = [
    path('', shop_views.index, name="Shop Home"),
    path('about/', shop_views.about, name="About Us"),
    path('contact/', shop_views.contact, name="Contact Us"),
    path('tracker/', shop_views.tracker, name="Tracking Status"),
    path('search/', shop_views.search, name="Search"),
    path('productview/', shop_views.product_view, name="Product View"),
    path('checkout/', shop_views.checkout, name="Checkout"),
]