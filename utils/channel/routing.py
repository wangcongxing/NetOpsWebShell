from django.urls import path
from utils.channel import websocket


websocket_urlpatterns = [
    path('webssh/', websocket.WebSSH),
]