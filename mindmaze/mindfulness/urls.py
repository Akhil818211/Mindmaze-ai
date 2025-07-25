from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_list_view, name='exercise_list'),
    path('<int:exercise_id>/', views.exercise_detail_view, name='exercise_detail'),
    path('', views.mindfulness_list, name='mindfulness_list'),
]
