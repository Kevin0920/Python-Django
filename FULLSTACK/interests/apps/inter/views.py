from django.shortcuts import render, HttpResponse, redirect

from .models import Users, Interests

from django.conf.urls import url

# Create your views here.
def index(request):
    context = {

        "allusers": Users.objects.all()
    }
    return render(request, 'inter/index.html', context)

def users(request):
    if request.method == "POST":
        username = request.POST['username']
        int_name = request.POST['int_name']
        
        print username, int_name
        answer = Users.objects.addUserInterest(username, int_name)

    return redirect("/")

def interest(request):
    pass
