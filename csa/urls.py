from django.urls import path
from . import views

urlpatterns = [
    path('admission/', views.admission),
    path('bca/', views.bca),
    path('bsc/', views.bsc),
    path('msc/', views.msc),


]