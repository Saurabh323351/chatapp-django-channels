from django.shortcuts import render

# Create your views here.

# chat/views.py
from django.shortcuts import render

def index(request):

    return render(request, 'chat/index.html', {})



def room(request, room_name):

    from django.contrib.auth.models import User
    # obj = User.objects.create(username="saurabh", password="1234", email="singh.saurabh3333@gmail.com")
    # obj.save()
    # print(obj.username, '--->obj')

    return render(request, 'chat/room.html', {
        'room_name': room_name,
    })