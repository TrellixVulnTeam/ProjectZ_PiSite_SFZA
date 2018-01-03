from django.shortcuts import render, redirect
from . import models
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from util_tools import wifi_util, user_util, hardware_util, plant_util


def index(request):
    context = {
        "sensor_list": hardware_util.get_sensors_status()
    }
    return render(request, 'Home/index.html', context)


def login(request):
    if user_util.get_users_name() != 'None':
        return redirect('/profile')

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        if user_util.check_user(username, password):
            user_util.login_user(username, "vasya")
            return redirect('/profile')

    return render(request, 'Home/login.html')


def message(request):
    return render(request, 'Home/message.html')


def change_assignment(request):
    context = {
        'msg': user_util.change_assignment()
    }
    return render(request, 'Home/message.html', context)


def wifi(request):
    if request.method == 'POST':
        wifi_name = request.POST["wifi_name"]
        password = request.POST["password"]

        pos = wifi_name.find(":")
        actual_wifi_name = wifi_name[:pos]

        answer = wifi_util.connect_to_wifi(actual_wifi_name, password)
        context = {
            'msg': answer
        }
        return render(request, 'Home/message.html', context)

    wifi_list = wifi_util.get_wifi_choices()
    context = {
        'choices': wifi_list,
        'choices_len': len(wifi_list)
    }
    print(context['choices'])
    return render(request, 'Home/wifi_select.html', context)


def profile(request):
    context = user_util.get_user_context()
    return render(request, 'Home/profile.html', context)


def logout(request):
    if wifi_util.get_users_name() != 'None':
        wifi_util.disconnect_user()

    return redirect('/')


def disconnect_wifi(request):
    wifi_util.disconnect_from_wifi()
    context = {
        'msg': "You have been disconnected from local wifi"
    }
    return render(request, 'Home/message.html', context)


def manage_plant(request):
    arr = hardware_util.get_last_sensor_update()
    context = {
        'arr_sensors': arr
    }
    return render(request, 'Home/manage_plant.html', context)


def get_sensors_status(request):
    try:
        model = models.CommandsToDo.objects.create(cmd_name="get_sensors_status", pi_mac=hardware_util.get_mac())
        model.save()
    except Exception as err:
        print(err)

    return redirect('/manage_plant')


def get_commands(request):
    pi_mac = request.GET['pi_mac']
    print("request for commands from: ", pi_mac)

    commands = models.CommandsToDo.objects.filter(pi_mac=pi_mac)

    commands_resp = []

    if commands.count() > 0:
        print("there are commands to do")
        for cmd in commands:
            commands_resp.append({"name": cmd.cmd_name})

        commands.delete()
        data = {
            'success': True,
            'commands': commands_resp
        }
    else:
        data = {
            'success': False,
        }

    return JsonResponse(data)


@csrf_exempt
def receive_and_save_sensors(request):
    data = json.loads(request.body)
    print(data)
    pi_mac = data['pi_mac']
    arr_sensor = data['arr_sensor']

    try:
        model = models.SensorsLogs.objects.create(heat=arr_sensor[0]['value'],
                                                  light=arr_sensor[1]['value'],
                                                  moist=arr_sensor[2]['value'],
                                                  rain=arr_sensor[3]['value'],
                                                  water_lvl=arr_sensor[4]['value'],
                                                  pi_mac=pi_mac)
        model.save()
        answer = {
            "success": True
        }
    except Exception as err:
        print(err)
        answer = {
            "success": False
        }
    return JsonResponse(answer)


def choose_profile(request):
    profile = plant_util.get_profile()
    # if request.method == 'POST':

    return render(request, 'Home/choose_profile.html')
