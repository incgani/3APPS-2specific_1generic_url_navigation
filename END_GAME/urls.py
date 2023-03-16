from django.urls import path
from END_GAME.views import *
app_name='END_GAME'
urlpatterns=[
    path('end_game/',end_game,name='end_game'),
]