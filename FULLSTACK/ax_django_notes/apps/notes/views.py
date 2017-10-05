from django.shortcuts import render, redirect
from .models import Note
# Create your views here.
def index(request):
    context = {
        'notes': Note.objects.all(),
        # 'new_post_form' : PostForm()
    }
    return render(request, 'notes/index.html', context)

def addNote(request):
    if request.method == "POST":
        Note.objects.newNote(request.POST['note'])
    context = {
    	'posts': Note.objects.all()
    }
    return render(request, 'notes/post_index.html', context)

def delnote(request,id):
    Note.objects.delNote(id)
    return redirect('/')
