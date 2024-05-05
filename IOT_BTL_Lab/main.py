import sys
from Adafruit_IO import MQTTClient

import time
import random

from uart import *

AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "QuangBang"
AIO_KEY = "aio_IJvL36JrbjOTKXHaHM3VqWIRm56h"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload, " , feed io: ", feed_id)
    if feed_id == "nutnhan2":
        if payload == "0":
            writeData("0")
        else: 
            writeData("1")



client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
sensor_type = 0
counter_ai = 5
ai_result = ""
previous_result = ""
while True:


    readSerial(client)

    time.sleep(1)
    pass