from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def admission(request):
    # print(type(request))
    # print('admisson room !')
    return HttpResponse("Admission room !")

def bca(request):
    return HttpResponse("Welcome to BCA")
    # print('Welcome to BCA')

def bsc(request):
    return HttpResponse("Welcome to BSC")
    # print('Welcome to BSC')

def msc(request):
    return HttpResponse("Welcome to MSC")
    # print('Welcome to MSC')

