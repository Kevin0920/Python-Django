from __future__ import unicode_literals

from django.db import models

import datetime
import bcrypt

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

todaySalt = ''
todayDate = ''


# Create your models here.
class userManager(models.Manager):
    def login(self,email,pw):
        e_mail = True
        pw_match = True
        empty = True

        user = ''

        if len(email) < 2 or len(pw) < 2:
            empty = False
        else:
            query = User.objects.filter(email=email)
            if len( query ) == 0:
                e_mail = False
            else:

                db_hashed = query[0].password

                if db_hashed != bcrypt.hashpw(pw.encode(), db_hashed.encode()):
                    pw_match = False
                else:
                    user = User.objects.get(email=email)

        answer = {
            "email": e_mail,
            "pwmatch": pw_match,
            "empty": empty,
            "user": user
        }
        return answer

    def reg(self,fname,lname,email,pw,repw):
        print fname,lname,email,pw,repw
        f_name = True
        l_name = True
        fl_name_alpha = True
        e_mail = True
        pw_length = True
        pw_match = True
        e_mail_uniq = True

        if len(fname)<2:
            f_name = False
        if len(lname)<2:
            l_name = False

        # is alphabetical string was imput
        if not str(fname).isalpha() or not str(lname).isalpha():
            fl_name_alpha = False

        # email validation
        try:
            validate_email(email)
        except:
            e_mail = False

        # the same emails
        if len(User.objects.filter(email=email))>0:
            e_mail_uniq = False

        # password match
        if pw != repw:
            pw_match = False
        if len(pw)<8:
            pw_length = False

        answer = {
            'fname': f_name,
            'lname': l_name,
            'fl_alpha': fl_name_alpha,
            'email': e_mail,
            'pw_length': pw_length,
            'pw_match': pw_match,
            'uniq_email': e_mail_uniq
        }

        return answer

    def addSecret(self,secret,id):
        if len(secret) > 5:
            thisUser = User.objects.get(id=id)
            Secret.objects.create(secret=secret,author=thisUser)
            return True
        else:
            return False

    def addLike(self,id,user_id):
        secret = Secret.objects.get(id=id)
        user = User.objects.get(id=user_id)

        user.liked.add(secret)


class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)


    objects = userManager()

class Secret(models.Model):
    secret = models.TextField()
    author = models.ForeignKey(User, related_name="secrets")

    likedBy = models.ManyToManyField(User, related_name="liked")

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)




    # def mss(self, id):
    #     checkToday = str(datetime.datetime.now().strftime('%D'))
    #     global todayDate
    #     global todaySalt
    #
    #     if todayDate != checkToday:
    #         todayDate = checkToday
    #         print todayDate
    #         todaySalt = bcrypt.gensalt()
    #         print todaySalt
    #     # if
    #
    # def esalt(self, id):
    #     self.mss(id)
    #     email = User.objects.get(id=id).email
    #     return bcrypt.hashpw(email.encode(), todaySalt)
    #     #  if expireTime != expireTime
    #
    # def trueSession(self,id,key):
    #     self.mss(id)
    #     if len( User.objects.filter(id=id) ) > 0:
    #         email = User.objects.get(id=id).email
    #         hashedEmail = bcrypt.hashpw(email.encode(), todaySalt)
    #         if key == hashedEmail:
    #             return True
    #         else:
    #             return False
