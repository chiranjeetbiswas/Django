from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

# rooms=[{'id': 1,'name':'lets learn python'},
#        {'id': 2,'name':'lets learn python'},
#        {'id': 3,'name':'lets learn python'},
#        {'id': 4,'name':'lets learn python'},
#        {'id': 5,'name':'lets learn python'},
#        {'id': 6,'name':'lets learn python'}]


def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)


def room(request,pk):
    rooms=Room.objects.get(id=pk)
    context={'rooms':rooms}
    return render(request,'base/room.html',context)

def createroom(request):
    context={}
    return render(request,'base/room_form.html',context)
