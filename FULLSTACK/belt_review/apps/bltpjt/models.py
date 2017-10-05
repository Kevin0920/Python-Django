from __future__ import unicode_literals

from django.db import models


import bcrypt

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your models here.
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


class reviewManager(models.Manager):
    def addReview(self,user_id, title,review,stars,author):
        t_itle = True
        r_eview = True
        t_itle_message = ''
        r_eview_message = ''

        if len(title) < 2:
            t_itle = False
            t_itle_message = "Please fill title field"
        elif len(review) < 10:
            r_eview = False
            r_eview_message = "Please review field"
        else:
            print user_id, title,review,stars,author

            author = Author.objects.create(name=author)
            book = Book.objects.create(title=title,author=author)
            user = User.objects.get(id=user_id)
            review = Review.objects.create(stars=int(stars),review=review,author=user,book=book,review_id=book)

            # review_id = models.ForeignKey(Book, related_name="reviewed")

            answer = book.id
            print "------finished creating---all records----"
            return answer

        answer = {
            "t_itle": t_itle,
            "r_eview": r_eview,
            "t_itle_message": t_itle_message,
            "r_eview_message": r_eview_message
        }
        return answer

class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    objects = userManager()

class Author(models.Model):
    name = models.CharField(max_length=255)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)

    author = models.ForeignKey(Author, related_name="book")

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()

    review_id = models.ForeignKey(Book, related_name="reviewed")
    author = models.ForeignKey(User, related_name="u_review")
    book = models.ForeignKey(Book, related_name="b_review")

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    objects = reviewManager()
