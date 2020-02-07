from django.shortcuts import render

# Create your views here.

# chat/views.py
from django.shortcuts import render
from rest_framework.decorators import api_view


# @api_view(['GET', 'POST'])
def index(request):

    print('-------->here',request.user)
    return render(request, 'chat/index.html', {})


# @api_view(['GET', 'POST'])
def room(request, room_name):

    from django.contrib.auth.models import User
    # obj = User.objects.create(username="saurabh", password="1234", email="singh.saurabh3333@gmail.com")
    # obj.save()
    # print(obj.username, '--->obj')

    return render(request, 'chat/room.html', {
        'room_name': room_name,
    })