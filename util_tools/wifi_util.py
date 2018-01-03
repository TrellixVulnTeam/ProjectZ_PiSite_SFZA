
from . import connect
from subprocess import check_output
import os
import time


def get_wifi_choices():
    try:
        wifi_list = connect.get_wifi_networks()
        return wifi_list
    except Exception as inst:
        print(inst)

    wifi_list = []
    return wifi_list


def connect_to_wifi(ssid, password):
    try:
        if password == "":
            return connect.connect(ssid)
        else:
            return connect.connect(ssid, password)
    except Exception as inst:
        print(inst)

    return "No wifi dongle"


def disconnect_from_wifi():
    os.system('sudo ifdown wlan0')
    time.sleep(2)
    os.system('sudo ifup wlan0')


def get_wifi_name():
    try:
        wifi_name = check_output(['iwgetid', '-r']).decode("utf-8")
        return wifi_name[:len(wifi_name)-1]
    except Exception as inst:
        print(inst)

    return "Not Connected"