from django.shortcuts import render
from . import utility
from . import models
from django.http import HttpResponse
from . import connect


def index(request):
    context = {
        "sensor_list": utility.get_sensors_status()
    }
    return render(request, 'Home/index.html', context)


def test(request):
    # x = connect.Search()
    return HttpResponse("lol")


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        if utility.check_user(username, password):
            context = {
                'msg': 'You successfully linked to your account'
            }
            model = models.AssignedTo.objects.create(username=username, actualName="vasya")
            model.save()
            return render(request, 'Home/message.html', context)

    return render(request, 'Home/login.html')


def message(request):
    return render(request, 'Home/message.html')


def wifi(request):
    if request.method == 'POST':
        wifi_name = request.POST["wifi_name"]
        password = request.POST["password"]

        pos = wifi_name.find(":")
        actual_wifi_name = wifi_name[:pos]

        answer = utility.connect_to_wifi(actual_wifi_name, password)
        context = {
            'msg': answer
        }
        return render(request, 'Home/message.html', context)

    context = {
        'choices': utility.get_wifi_choices(),
    }
    print(context['choices'])
    return render(request, 'Home/wifi_select.html', context)
