from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list_view, name='game_list'),
    path('<int:game_id>/play/', views.play_game_view, name='play_game'),
]
