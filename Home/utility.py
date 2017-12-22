
from . import models
from subprocess import check_output

def get_wifi_choices():
    wifilist = {
        'wifi1': False,
        'wifi2': True
    }
    return wifilist.items()


def check_login():
    model = models.AssignedTo.objects.get()
    print(model)
    if model is None:
        return 'None'

    return model.actualName

def get_sensors_status():
    sensor_list = {
        'Soil Moisture': False,
        'Heat': True,
        'Rain': True,
        'Pump': False,
        'Light': True,
        'Water Amount': False
    }
    return sensor_list.items()


def check_user(username, password):
    return True


def get_wifi_name():
    try:
        wifi_name = check_output(['iwgetid','-r'])
        return wifi_name
    except Exception as inst:
        print(inst)

    return "Not connected"

