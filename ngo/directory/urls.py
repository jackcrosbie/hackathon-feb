from . import views
from django.urls import path

urlpatterns = [
    path('', views.organisations, name='orgs'),
    path('events/', views.events, name='events'),
]
