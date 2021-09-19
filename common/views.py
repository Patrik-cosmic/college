from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("Welcome to CTCJ college")
    return render(request, 'college/home.html')