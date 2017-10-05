from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# new commetn
import bcrypt
# Generate salt, and after use it in models.py too
# salt = bcrypt.gensalt()

from django.db.models import Count

from .models import User, Author, Book, Review

def index(request):

    context = {
        "users": User.objects.all()
    }
    if "id" in request.session:
        return redirect('/books')
    else:
        return render(request, 'bltpjt/index.html', context)


def books(request):
    if "id" in request.session:

        context = {
            "user": User.objects.get(id=request.session['id'])
        }
        return render(request, 'bltpjt/success.html', context)
    else:
        return redirect("/")


def addbookrview(request):
    if request.method == "POST":
        user_id = request.session['id']
        title = request.POST['title']
        review = request.POST['review']
        stars = request.POST['stars']

        if len(request.POST['author'])>0:
            author = request.POST['author']
        elif request.POST['author_existed'] != "empty":
            author = request.POST['author_existed']
        else:
            messages.add_message(request, messages.ERROR, "Don't leave author field empty")
            return redirect('/addbookrview')

        answer = Review.objects.addReview(user_id, title,review,stars,author)
        print "----answer---"
        print answer
        print "-------"

        if type(answer) != dict:
            url = "/books/" + str(answer)
            print "-------"
            print url
            print "-------"
            return redirect(url)
        else:
            messages.add_message(request, messages.ERROR, "You did something wrong man")
            return redirect('/addbookrview')

    else:
        if "id" in request.session:

            context = {
                "books": Book.objects.all()
            }
            return render(request, 'bltpjt/addbookrview.html', context)
        else:
            return redirect("/")

def one_book(request,id):
    context = {
        "book": Book.objects.filter(id=id),
        'reviews':Book.objects.all().filter(id=id),
        # 'books':Review.objects.all(),
        # 'reviews':Review.objects.filter("book__id"=id)
    }
    return render(request, 'bltpjt/bookpage.html', context)

def delbook(request,id):
    Book.objects.filter(id=id).delete()
    return redirect('/addbookrview')

def delreview(request,id):
    book_id = Review.objects.filter(id=id)
    print book_id
    # Review.objects.filter(id=id).delete()
    # url = '/books/' + book_id
    # return redirect(url)
    return redirect("/")

def logout(request):
    del request.session['id']
    return redirect('/')

def login(request):
        if request.method == "POST":
            email = request.POST['email']
            pw = request.POST['pw']

            answer = User.objects.login(email,pw)

            if not answer['email']:
                messages.add_message(request, messages.ERROR, "We don't have such user with that email")
                return redirect('/')
            elif not answer['empty']:
                messages.error(request, "You can't enter empty or short value")
                return redirect('/')
            elif not answer['pwmatch']:
                messages.add_message(request, messages.ERROR, "The password you entered don't match this email")
                return redirect('/')
            elif  answer['user'] != '':
                messages.success(request, "Successfully logined!")
                request.session['id'] = answer['user'].id

                return redirect('/books')

        return redirect('/')

def reg(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pw = request.POST['pw']
        repw = request.POST['repw']

        answer = User.objects.reg(fname,lname,email,pw,repw)

        if not answer['fname'] or not answer['lname']:
            messages.add_message(request, messages.ERROR, 'Please enter string at least 3 characters in Name and Lastname fields')
        elif not answer['fl_alpha']:
            messages.add_message(request, messages.ERROR, 'Use only alphabet characters')
        elif not answer['email']:
            messages.add_message(request, messages.ERROR, 'Email is not valid')
        elif not answer['pw_length']:
            messages.add_message(request, messages.ERROR, 'Password is too short')
        elif not answer['pw_match']:
            messages.add_message(request, messages.ERROR, "Passwords don't match")
        elif not answer['uniq_email']:
            messages.add_message(request, messages.ERROR, "We already have this email in data base")
        else:
            # if everything is good
            hashed_pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())

            User.objects.create(
                fname=fname,
                lname=lname,
                email=email,
                password=hashed_pw
            )

            # User.objects.mss(email)
            request.session['id'] = User.objects.get(email=email).id

            messages.add_message(request, messages.SUCCESS, "Successfully registered!")
            return redirect('/books')

    return redirect('/')
