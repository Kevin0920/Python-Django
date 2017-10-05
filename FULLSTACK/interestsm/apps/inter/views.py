from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Users, Interests
# Create your views here.
def index(request):
    
    return render(request, 'inter/index.html')

def submit(request):
    if request.method == "POST":
        Users.objects.submit(request.POST)
        
        return redirect('/users')
        

def users(request):
    
    users = Users.objects.all()
    content = {'users': users}
    return render(request, 'inter/users.html', content)

def interests(request, name):
    interests = Interests.objects.filter(users__name = name)
    content = {'interests': interests, 'name': name}
    return render(request, 'inter/interest.html', content)
