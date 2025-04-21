from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms=[{'id': 1,'name':'lets learn python'},
       {'id': 2,'name':'lets learn python'},
       {'id': 3,'name':'lets learn python'},
       {'id': 4,'name':'lets learn python'},
       {'id': 5,'name':'lets learn python'},
       {'id': 6,'name':'lets learn python'}]


def home(request):
    context={'rooms':rooms}
    return render(request,'base/home.html',context)


def room(request,pk):
    return render(request,'base/room.html')
