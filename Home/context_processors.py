from . import utility


def my_context(request):
    context_data = {
        'wifi_name': utility.get_wifi_name(),
        'login': utility.get_users_name()
    }

    return context_data

