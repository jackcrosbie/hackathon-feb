from . import views
from django.urls import path

urlpatterns = [
    path('events/', views.events, name='events'),
]
