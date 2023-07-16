import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Profile
from asgiref.sync import sync_to_async, async_to_sync


connected_users = {}


class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # Add user's connection object to connected_users dictionary

        user_id = self.scope['user'].id
        
        if user_id not in connected_users:
            connected_users[user_id] = [self.channel_name]
        else:
            connected_users[user_id].append(self.channel_name)

        pro_obj = await sync_to_async(Profile.objects.filter(user_id=user_id).first)()
        pro_obj.is_online = True
        await sync_to_async(pro_obj.save)()
        

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        # Remove user's connection object from connected_users dictionary
        user_id = self.scope['user'].id
        if user_id in connected_users:
            pro_obj = await sync_to_async(Profile.objects.filter(user_id=user_id).first)()
            pro_obj.is_online = False
            await sync_to_async(pro_obj.save)()
            connected_users[user_id].remove(self.channel_name)
        

       

        
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = self.scope["user"].username
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message,'username': username}
        )
        


    # Receive message from room group
    async def chat_message(self, event):
        message = event.get("message")
        username = event.get("username")
        await self.send(text_data=json.dumps({"message": message, "username": username}))
        



class NotificationConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = 'notifications'
        self.room_group_name = 'notifications_group'

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

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'notification_message',
                'message': message
            }
        )

    async def notification_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))