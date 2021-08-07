from django.urls import re_path
#'re_path' means 'relative path'
from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer),
    #In the above line we created a relative path with a variable named as 'room_name' which takes whatever string is entered after the word 'chat/'. The '$' signs means the urlpattern ends there.
]