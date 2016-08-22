from __future__ import unicode_literals
import re
from django.db import models
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
from django.contrib.auth import password_validation
# Create your models here.
class UserManager(models.Manager):
    def register(request, reg_data):
        errors = []
        name = reg_data['name']
        username = reg_data['username']
        password = reg_data['password']
        confirm_password = reg_data['confirm_password']
        if not len(name)>3:
            errors.append("Please enter a valid name")
        if not len(username)>3:
            errors.append("Please enter a valid username")
        if not (len(password)>8) and (password == confirm_password):
            errors.append("Please enter a valid password")
        if errors:
            return (True, errors)
        else:
            return (False, reg_data)
    def login(self, log_data):
        errors = []
        username = log_data['username']
        user = self.filter(username=username)
        password = log_data['password']
        if (len(user)>0) and bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password:
            return (True, user[0])
        else:
            errors.append("Invalid information, try again")
            return (False, errors)

    pass
class User(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    travel = models.ManyToManyField('travel_bud.Travel', related_name = 'traveluser')
    UserManager= UserManager()
    objects = models.Manager()
