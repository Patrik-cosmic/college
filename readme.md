# Roadmap so far

- Install Django: pip install Django
- Create a project: django-admin startproject college
- Run the server: python3 manage.py runserver
- Create an app: python3 manage.py startapp csa

## Setup the apps
- create urls.py for each app
- Register the apps on settings.py (INSTALLED_APPS)

## Setup project.urls (college.map)

- syntax : path('pattern/',include('app.urls')) 
   - include ::::: from django.urls import include  

## Setup app.urls (dept.map)

- syntax : path('pattern/', views.func_name)
views ::::: from . import views :::: "." means from current directory 

## views.py
	from django.http import HttpResponse

	def func_name(request):
            return HttpResponse("html")		
