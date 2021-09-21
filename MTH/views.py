from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def admission(request):
    return render(request, ('mth/mth.html'))
def msc(request):
    return render(request, ('mth/msc.html'))
def bsc(request):
    return render(request, ('mth/bsc.html'))