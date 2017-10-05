from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def addUserInterest(self,username, interest):
        print username, interest

        # check if we have such user in DB
        if len( Users.objects.filter(name=username) ) == 0:
            Users.objects.create(name=username)

        # Check if we have such interest in DB
        if len( Interests.objects.filter(iname=interest) ) == 0:
            Interests.objects.create(iname=interest)

        # Preparing for making relationships
        user = Users.objects.get(name=username)
        interest = Interests.objects.get(iname=interest)

        interest.all_users.add(user)


class Users(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Interests(models.Model):
    iname = models.CharField(max_length=100)
    all_users = models.ManyToManyField(Users, related_name="all_interest")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
