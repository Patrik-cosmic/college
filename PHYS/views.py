from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, ('phys/phys_home.html'))

def bsc(request):
    return render(request, ('phys/Bsc.html'))

def msc(request):
    return render(request, ('phys/msc.html'))