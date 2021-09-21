# Roadmap so far
---
## Day 1
---
> **Install Django**
   - `pip install Django`
> **Create a project**
   - `django-admin startproject college`
> **Run the server**
   - `python3 manage.py runserver`
> **Create an app**
 - `python3 manage.py startapp csa`

## Setup the apps
- create urls.py for each app
- Register the apps on settings.py (INSTALLED_APPS)

## Setup project.urls (college.map)

> syntax : 
- `path('pattern/',include('app.urls'))`
   - `include > from django.urls import` include  

## Setup app.urls (dept.map)

> syntax 
 - ` path('pattern/', views.func_name)`
    - `views > from . import views`
       - `"." means from current` directory 

## views.py
	from django.http import HttpResponse

	def func_name(request):
            return HttpResponse("html")		

---
## Day 2
---
> **Setup templates**
- Change the settings.py
``` 
   TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # change here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
] 
``` 
- Make a folder named "templates" on the root level of your project 

> **Render templates from views.py**
```
from django.shortcuts import render
return render(request, 'csa/bca.html') # render(request, 'location_of_the_template')
```

> **Give name to url**
- Open urls.py
- Add another keyword arg `name` to the `path()` 
    - `path('', views.home, name='csa_home')`# usage
- Now use `{% url 'csa_home' %}` inside your html page to point to the path "`csa_home`"
    -  `{% url 'name_of_the_path' %}` # usage

> **Serve staticfiles**

- Open settings.py
- Add `STATIC_URL = '/static/'`
- Create a folder named "static" within any app.
- Add `{% load static %}` tag at the very beginning, inside the html page where you need to serve static files.
- Use ` {% static 'path_to_static_files' %}"` finally.

