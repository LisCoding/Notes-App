from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.core import serializers

def index(request):
    return render(request,'notes_app/index.html')

def create_note(request):
    Note.objects.create(title=request.POST["title"])
    notes = Note.objects.all()
    return render(request, "notes_app/notes.html", {"notes": notes})

def delete_note(request, id):
    Note.objects.get(id=id).delete()
    notes = Note.objects.all()
    return render(request, "notes_app/notes.html", {"notes": notes})
