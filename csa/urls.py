from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='csa_home'),
    path('bca/', views.bca, name='bca'),
    path('bsc/', views.bsc, name='bsc'),
    path('msc/', views.msc, name='msc'),


]