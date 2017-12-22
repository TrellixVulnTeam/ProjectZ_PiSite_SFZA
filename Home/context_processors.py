from . import utility


def my_context(request):
    context_data = {
        'ppc': utility.get_wifi_name(),
        'login': utility.check_login()
    }

    return context_data