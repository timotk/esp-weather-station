import utime
import dht
import machine
from umqtt.simple import MQTTClient

import secrets


TOPIC = "channels/" + secrets.CHANNEL_ID + "/publish/" + secrets.WRITE_API_KEY


def log_temperature():
    device = dht.DHT11(machine.Pin(14))  # Pin 14 corresponds to board pin D5

    client = MQTTClient("umqtt_client", secrets.SERVER)

    while True:
        device.measure()
        temperature = device.temperature()
        humidity = device.humidity()

        payload = "field1="+str(temperature)+"&field2="+str(humidity)
        client.connect()
        client.publish(TOPIC, payload)

        utime.sleep(300)

    client.disconnect()
