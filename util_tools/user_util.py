
from Home import models


def login_user(username, actual_Name):
    model = models.AssignedTo.objects.create(username=username, actualName=actual_Name)
    model.save()


def check_user(username, password):
    return True


def get_user():
    model = models.AssignedTo.objects.filter()

    if model.count() > 0:
        return models.AssignedTo.objects.get()

    return None


def disconnect_user():
    model = models.AssignedTo.objects.get()
    model.delete()
    return True


def get_users_name():
    model = models.AssignedTo.objects.filter()

    if model.count() > 0:
        model = models.AssignedTo.objects.get()
        return model.actualName

    return 'None'


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
