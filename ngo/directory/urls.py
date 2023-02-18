from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('events/', views.events, name='events'),
    path('donate/', views.donate, name='donate'),
]
