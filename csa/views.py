from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'csa/csa.html')

def bca(request):
     return render(request, 'csa/bca.html')

def bsc(request):
    return render(request, 'csa/bsc.html')

def msc(request):
     return render(request, 'csa/msc.html')

