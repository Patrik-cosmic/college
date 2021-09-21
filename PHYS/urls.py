from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name='phys_home'),
    path('bsc/', views.bsc, name = 'phys_bsc'),
    path('msc/', views.msc, name = 'phys_msc',),
    ]