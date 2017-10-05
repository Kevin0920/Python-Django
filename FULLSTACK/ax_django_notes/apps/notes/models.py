from __future__ import unicode_literals

from django.db import models

class userManager(models.Manager):
    def newNote(self,text):
        Note.objects.create(text=text)
        return ''

    def delNote(self,id):
        Note.objects.filter(id=id).delete()
        return ''

# Create your models here.
class Note(models.Model):
    text = models.TextField()

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    objects = userManager()
