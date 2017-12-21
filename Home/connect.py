import wifi


def get_wifi_networks():
    wifi_list = {}

    cells = wifi.Cell.all('wlan0')
    for cell in cells:
        wifi_list[cell.ssid] = cell.encrypted

    print(wifi_list.items())
    return wifi_list.items()


def Search():
    wifilist = []

    cells = wifi.Cell.all('wlan0')
    for cell in cells:
        wifilist.append(cell)

    return wifilist


def FindFromSavedList(ssid):
    cell = wifi.Scheme.find('wlan0', ssid)
    if cell:
        return cell
    return False


def Delete(ssid):
    if not ssid:
        return False
    cell = FindFromSavedList(ssid)
    print(cell)
    if cell:
        cell.delete()
        return True
    return False

def FindFromSearchList(ssid):
    wifilist = Search()

    for cell in wifilist:
        if cell.ssid == ssid:
            return cell

    return False

def connect(ssid, password=None):
    Delete(ssid)
    cell = FindFromSearchList(ssid)

    if cell:
        print(cell)
        if cell.encrypted:
            if password:
                scheme = Add(cell,password)
                try:
                    scheme.activate()

                #wrong password
                except wifi.exceptions.ConnectionError:
                    Delete(ssid)
                    return False

                return "Connected to: "+ssid
        else:
            scheme = Add(cell)
            try:
                scheme.activate()
            except wifi.exceptions.ConnectionError:
                Delete(ssid)
                return False

            return "Connected to: "+ssid

    return False

def Add(cell,password=None):
    if not cell:
        return False

    scheme = wifi.Scheme.for_cell('wlan0', cell.ssid, cell, password)
    scheme.save()
    return scheme


# def __main__():
# 	x = 1
# 	while x!='0':
# 		x = input('Please enter command:')
# 		if x=='connect':
# 			y = input('Please enter ssid:')
# 			z = input('Please enter password:')
# 			print(connect(y,z))
# 		elif x=='search':
# 			print(Search())
#
# __main__()
