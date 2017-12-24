
from . import connect
from . import models
from subprocess import check_output


def get_wifi_choices():
    try:
        wifi_list = connect.get_wifi_networks()
        return wifi_list.items()
    except Exception as inst:
        print(inst)

    wifi_list = {
        'wifi1': False,
        'wifi2': True
    }
    return wifi_list.items()


def change_assignment():
    model = models.AssignedTo.objects.get()
    if model.linked:
        msg = 'You successfully unlinked the device from your account'
        model.linked = False
    else:
        msg = 'You successfully linked the device to your account'
        model.linked = True
    model.save()

    return msg


def get_user():
    model = models.AssignedTo.objects.filter()

    if model.count() > 0:
        return models.AssignedTo.objects.get()

    return None


def get_user_context():
    user = get_user()

    if user is not None:
        model = models.AssignedTo.objects.get()
        context = {
            "users_name": model.actualName,
            'log_msg': 'Log out',
            'log_icon': 'power_settings_new',
            'log_link': '/logout/'
        }
        if model.linked:
            context['msg'] = 'Unlink from acc'
            context['icon'] = 'leak_remove'
        else:
            context['msg'] = 'Link to my acc'
            context['icon'] = 'leak_add'

        return context
    else:
        context = {
            "users_name": None,
            'log_msg': 'Log in',
            'log_icon': 'account_circle',
            'log_link': '/login/'
        }
    return context


def get_users_name():
    model = models.AssignedTo.objects.filter()

    if model.count() > 0:
        model = models.AssignedTo.objects.get()
        return model.actualName

    return 'None'


def disconnect_user():
    model = models.AssignedTo.objects.get()
    model.delete()
    return True


def get_sensors_status():
    sensor_list = [{'sensor_name': 'Soil Moisture', 'status': False, 'icon': 'opacity'},
           {'sensor_name': 'Heat', 'status': True, 'icon': 'whatshot'},
           {'sensor_name': 'Rain', 'status': True, 'icon': 'beach_access'},
           {'sensor_name': 'Pump', 'status': False, 'icon': 'power'},
           {'sensor_name': 'Light', 'status': True, 'icon': 'wb_sunny'},
           {'sensor_name': 'Water Amount', 'status': False, 'icon': 'format_color_fill'},
           ]

    return sensor_list


def check_user(username, password):
    return True


def get_wifi_name():
    try:
        wifi_name = check_output(['iwgetid', '-r'])
        return wifi_name
    except Exception as inst:
        print(inst)

    return "Not connected"


def connect_to_wifi(ssid, password):
    try:
        if password == "":
            return connect.connect(ssid)
        else:
            return connect.connect(ssid, password)
    except Exception as inst:
        print(inst)

    return "No wifi dongle"

