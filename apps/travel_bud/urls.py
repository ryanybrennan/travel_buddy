from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^main/$', views.login_reg, name = 'login_reg'),
    url(r'^travels$', views.home, name = 'travel_dash'),
    url(r'^travels/add$', views.add, name = 'add_trip'),
    url(r'^travels/destination/(?P<id>\d+)$', views.destination, name= 'destination'),
    url(r'^create$', views.create, name = 'create'),
    url(r'^join/(?P<id>\d+)$', views.join, name = 'join_trip')
]
