import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class PokerConsumer(WebsocketConsumer):
    def connect(self):
        self.table_name = self.scope['url_route']['kwargs']['table_name']
        self.table_group_name = f'room_{self.table_name}'

        # Join table group
        async_to_sync(self.channel_layer.group_add)(
            self.table_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave table group
        async_to_sync(self.channel_layer.group_discard)(
            self.table_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to table group
        async_to_sync(self.channel_layer.group_send)(
            self.table_group_name,
            {
                'type': 'room_message',
                'message': message
            }
        )

    # Receive message from table group
    def room_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
