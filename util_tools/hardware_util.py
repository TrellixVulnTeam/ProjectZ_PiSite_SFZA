
from Home import models


def get_sensors_status():
    sensor_list = [{'sensor_name': 'Soil Moisture', 'status': False, 'icon': 'opacity'},
           {'sensor_name': 'Heat', 'status': True, 'icon': 'whatshot'},
           {'sensor_name': 'Rain', 'status': True, 'icon': 'beach_access'},
           {'sensor_name': 'Pump', 'status': False, 'icon': 'power'},
           {'sensor_name': 'Light', 'status': True, 'icon': 'wb_sunny'},
           {'sensor_name': 'Water Amount', 'status': False, 'icon': 'format_color_fill'},
           ]

    return sensor_list


def get_last_sensor_update():
    model = models.SensorsLogs.objects.all()

    if model.count() > 0:
        return model.last()

    return None


def get_mac(interface='eth0'):
    # Return the MAC address of the specified interface
    try:
        mac_address = open('/sys/class/net/%s/address' % interface).read()
    except Exception as ex:
        print(ex)
        mac_address = "00:00:00:00:00:00"
    return mac_address[0:17]