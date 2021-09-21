from django.urls import path
from . import views

urlpatterns = [
    path('', views.admission, name = 'csa_home'),
    path('bsc/', views.bsc, name = 'bsc'),
    path('msc/', views.msc, name = 'msc'),
    path('bca/', views.bca, name = 'bca'),
]