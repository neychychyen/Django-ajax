from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_mesages, name='get_all_messages'),
    path('send/', views.send_message, name='send_message'),

]