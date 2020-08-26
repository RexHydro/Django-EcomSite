from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="Shophome"),
    path('about', views.about, name="about us"),
    path('contact/', views.contact, name="contact us"),
    path('tracker/', views.tracker, name="tracking status"),
    path('search/', views.search, name="search"),
    path('productview/', views.prodview, name="search"),
    path('checkout/', views.checkout, name="checkout"),
    # path('checkout', views.index, name="search"),



]
