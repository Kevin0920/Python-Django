from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def submit(self, post_data):
        # check if the interest exists
        if len(Interests.objects.filter(name = post_data['interest'])) == 0:
            Interests.objects.create(name = post_data['interest'])
        #check if the user exists
        if len(Users.objects.filter(name = post_data['user'])) == 0:
            Users.objects.create(name = post_data['user'])
        
        #check if the user exists with associated interest
        if len(Interests.objects.filter(name = post_data['interest'], users__name = post_data["user"]))==0:
            user = Users.objects.get(name = post_data['user'])
            interest = Interests.objects.get(name = post_data['interest'])
            interest.users.add(user)
        
class Users(models.Model):
    name = models.CharField(max_length = 30)
    objects = UserManager()

class Interests(models.Model):
    name = models.CharField(max_length = 30)
    users = models.ManyToManyField(Users, related_name = 'interests')
    objects = UserManager()