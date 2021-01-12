from django.urls import path
from . import views

app_name ='AnonMessager'
urlpatterns = [
    path('', views.loginFunction, name = 'login'),
    path('<str:username>/', views.sendMessage , name='sendMessage'),
    path('<str:username>/messages', views.messages, name='message'),
    path('j0inn', views.join, name = 'joinen'),
    
]