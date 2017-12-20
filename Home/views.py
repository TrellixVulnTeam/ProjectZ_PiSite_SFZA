from django.shortcuts import render
from . import utility
from . import models
from django.http import HttpResponse
from . import connect

def index(request):
    return render(request, 'Home/index.html')


def test(request):
    # x = connect.Search()
    return HttpResponse("lol")


def login(request):
    utility.check_login()
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

        print(wifi_name)

    context = {
        'choices': utility.get_wifi_choices(),
    }
    print(context['choices'])
    return render(request, 'Home/wifi_select.html', context)
