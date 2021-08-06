# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })

def home(request):
    return render(request, 'draw/home.html')

def create(request):
    return render(request, 'draw/create.html')

def define(request):
    return render(request, 'draw/define.html')

def sentence(request):
    return render(request, 'draw/sentence.html')

def saved(request):
    return render(request, 'draw/saved.html')
