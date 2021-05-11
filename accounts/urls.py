from django.contrib import admin
from django.urls import path
from . import views

# create function views.py
urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
]