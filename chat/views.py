from django.shortcuts import render

# Create your views here.
import jwt,pprint,json

# chat/views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageModelSerializer
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
    print(request.get_host())
    # print(dir(request))
    token=request.GET['token']
    payload = jwt.decode(token, 'its a secret', algorithms=['HS256'])
    user_obj = User.objects.get(id=payload['id'])
    user_messages=Message.objects.filter(author=user_obj)
    # serializer=MessageModelSerializer(user_messages,many=True)

    print(user_messages,'------->user_messages')

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'user':user_obj,
        'user_messages':user_messages
    })