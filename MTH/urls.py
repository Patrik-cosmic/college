from django.urls import path
from . import views

urlpatterns = [
    path('', views.admission, name = 'math_home'),
    path('bsc/', views.bsc, name = 'math_bsc'),
    path('msc/', views.msc, name = 'math_msc'),
]