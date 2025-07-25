from django.urls import path
from . import views

urlpatterns = [
    path('user-progress/', views.user_progress_view, name='user_progress'),
]
