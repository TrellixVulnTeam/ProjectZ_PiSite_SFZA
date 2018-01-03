from util_tools import user_util, wifi_util


def my_context(request):
    context_data = {
        'wifi_name': wifi_util.get_wifi_name(),
        'login': user_util.get_users_name()
    }

    return context_data

