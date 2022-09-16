from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='TEST HOME'),
	path('room/', views.room, name='TEST ROOM'),
]