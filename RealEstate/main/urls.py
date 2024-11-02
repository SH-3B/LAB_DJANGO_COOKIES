from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('properties/', views.properties, name='properties'),
    path('dark/', views.dark_mode, name='dark_mode'),
    path('light/', views.light_mode, name='light_mode'),
]