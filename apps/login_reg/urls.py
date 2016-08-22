from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^process/$', views.process, name = 'register'),
    url(r'^login/$', views.login, name = 'login'),
]
