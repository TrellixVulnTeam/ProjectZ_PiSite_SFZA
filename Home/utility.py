
from . import models
from . import connect


def get_wifi_choices():
    wifilist = {
        'wifi1': False,
        'wifi2': True
    }
    return wifilist.items()


def check_login():
    model = models.AssignedTo.objects.get()
    if model is not None:
        print('hui')



def check_user(username, password):
    return True

