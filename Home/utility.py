
from . import models


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




def check_user(username, password):
    return True

