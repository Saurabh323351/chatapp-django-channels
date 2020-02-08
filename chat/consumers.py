# chat/consumers.py
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# import json,pprint

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         pprint.pprint(self.scope,indent=4)
#         print(self.scope['headers'][0])
#         host_=self.scope['headers'][0]
#         print(host_[1])
#         dir(self.channel_name)
#         dir(self)
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         self.accept()
#
#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         print('--->receive',text_data)
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#
#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']
#
#         print('====>chat_message',event)
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))


from channels.generic.websocket import AsyncWebsocketConsumer
import json,pprint
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):


    async def connect(self):


        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        pprint.pprint(self.scope, indent=4)
        # print((self.scope['query_string']).decode('utf-8'))
        print(self.scope['user'],'---->connect')

        # host_=self.scope['headers'][0]
        # print(host_[1])
        # dir(self.channel_name)
        # dir(self)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(self.scope['user'],'receive user')

        # Send message to room group
        author_obj = self.scope['user']

        print("*" * 40)
        print(author_obj)
        print("*" * 40)
        from django.contrib.auth.models import User

        user_obj = User(id=author_obj.id)

        message_obj = Message.objects.create(content=message, author=user_obj)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )


    # Receive message from room group
    async def chat_message(self, event):

        message = event['message']
        print(self.scope['user'], 'chat_message user')




        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

