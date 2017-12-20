
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('wifi/', views.wifi, name='wifi'),
    path('test/', views.test, name='test'),
    path('message/', views.message, name='message'),
]
