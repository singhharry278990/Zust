from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]