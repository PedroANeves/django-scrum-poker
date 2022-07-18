from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/poker/table/(?P<table_name>\w+)/$', consumers.PokerConsumer.as_asgi()),
]