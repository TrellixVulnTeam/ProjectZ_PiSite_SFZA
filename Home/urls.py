
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('wifi/', views.wifi, name='wifi'),
    path('message/', views.message, name='message'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('assign/', views.change_assignment, name='change_assignment'),
]
