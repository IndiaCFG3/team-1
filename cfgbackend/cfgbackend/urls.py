"""cfgbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('users/', views.userList.as_view()),
    path('create-course-backend',views.createCourse),
    path('create-course',views.index),
    path('dashboard/',views.Dashboard),
    url('videos/', views.videoList.as_view()),
    path('create-video',views.uploadVideo),
    path('create-video-backend',views.uploadVideoBE),
]
