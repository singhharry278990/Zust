from django.urls import path

from . import consumers

websocket_urlpatterns = [
	path(r'ws/group/$', consumers.Calculator.as_asgi()),
]
