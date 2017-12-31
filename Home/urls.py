
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
    path('disconnect_wifi/', views.disconnect_wifi, name='disconnect_wifi'),
    path('manage_plant/', views.manage_plant, name='manage_plant'),
    path('get_sensors_status/', views.get_sensors_status, name='get_sensors_status'),
    path('get_commands/', views.get_commands, name='get_commands'),
    path('receive_and_save_sensors/', views.receive_and_save_sensors, name='receive_and_save_sensors'),
]
