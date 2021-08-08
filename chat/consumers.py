from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #In the code mentioned below we are just extracting the value of 'room_name' variable stored in the url patterns which is entered.
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        #In the code mentioned below we are just assigning the value of 'room_name' extracted in the above line to the 'room_group_name' variable.
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            #The channel_name attribute contains a pointer to the channel layer instance and the channel name which will reach the consumer.
            self.channel_name
        )

        # In the code mentioned below we are just accepting the connection request.
        await self.accept()

        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'tester_message',
        #         'tester': 'Hello world!',
        #     }
        # )


    # async def tester_message(self, event):
    #     tester = event['tester']

    #     await self.send(text_date=json.dumps({
    #         'tester':tester,
    #     }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chatroom_message',
                'message':message,
                'username': username,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message':message,
            'username': username,
        }))
    
    pass


