from __future__ import unicode_literals
from ..login_reg.models import User
from django.db import models
from datetime import datetime, timedelta, time, date
from time import strftime
class TravelManager(models.Manager):
    def trip(request, trip_data):
        errors = []
        destination = trip_data['destination']
        description = trip_data['description']
        travel_from = trip_data['travel_from']
        travel_to = trip_data['travel_to']
        now = strftime("%Y-%m-%d")
        if not len(destination)>0:
            errors.append("Please enter a valid destination")
        if not len(description)>0:
            errors.append("Please enter a valid description")
        if travel_from == "" or travel_to == "":
            errors.append("Please enter a date, stupid")
            print now
        if not (trip_data['travel_from'] < trip_data['travel_to']):
            errors.append("You are not a time traveler")
        if not (travel_from > now):
            errors.append("You are not a time traveler")
        if errors:
            return (True, errors)
        else:
            return (False, trip_data)

    pass
class Travel(models.Model):
    destination = models.CharField(max_length = 50)
    description = models.TextField()
    travel_from = models.DateField()
    travel_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    people = models.ManyToManyField('login_reg.User', related_name='usertravel')
    user = models.ForeignKey('login_reg.User', related_name = 'traveller')

    TravelManager= TravelManager()
    objects = models.Manager()
# class Traveluser(models.Model):
#     user = models.ForeignKey('login_reg.User', related_name= 'usertravel')
#     travel = models.ForeignKey('Travel', related_name= 'traveluser')
#     created_at = models.DateTimeField(auto_now_add= True)
#     updated_at = models.DateTimeField(auto_now = True)
