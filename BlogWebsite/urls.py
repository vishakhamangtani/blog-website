"""
URL configuration for BlogWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blogg.views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('./admin/', admin.site.urls),
     path('index/<pk>', index, name='index'),
     path('index/', index, name='index'),
     path('blogs/<pk>', blogs, name='blogs'),
     path('login/', login, name='login'),
     path('success/', success, name='success'),
     path('', signup, name='signup'),
     path('texteditor/', texteditor, name='texteditor'),
     path('my_blogs/', my_blogs, name='my_blogs'),
      path('partial_template/<str:category>/', partial_template, name='partial_template'),
      path('edit_profile/', edit_profile, name='edit_profile'),
      path('search/', search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

