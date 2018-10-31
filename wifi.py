import network
import secrets


def connect():
    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("Already connected!")
        return

    print("Connecting to {}...".format(secrets.SSID))
    station.active(True)
    station.connect(secrets.SSID, secrets.PASSWORD)

    while station.isconnected() == False:
        pass

    print("Connection successful!")
    print(station.ifconfig())
