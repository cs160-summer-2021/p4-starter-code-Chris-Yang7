# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('define/', views.define, name='define'),
    path('sentence/', views.sentence, name='sentence'),
    path('saved/', views.saved, name='saved')
]
