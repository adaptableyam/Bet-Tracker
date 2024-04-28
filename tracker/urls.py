from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-bet/', views.add_bet, name='add-bet'),
]
