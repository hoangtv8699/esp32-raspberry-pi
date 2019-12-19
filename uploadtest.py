import random
import serial
import time
import urllib.request
import os
import json

#
# ser = serial.Serial(
#     port='/dev/ttyUSB0',
#     baudrate = 9600,
# )
key = '3VCJACKUH9UCEOCB'  # Put your API Key here
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % key


def readData():
    read_serial = ser.readline()
    j = json.loads(read_serial)
    return j


def thermometer(j):
    while True:
        try:
            # Sending the data to thingspeak
            conn = urllib.request.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s' % (
            j['temp'], j['humidity'], j['light'], j['ec'], j['ph'], j['waterTemp']))
            print(j['temp'], j['humidity'], j['light'], j['ec'], j['ph'], j['waterTemp'])
            # Closing the connection
            conn.close()
        except Exception as e:
            print(e)
            print("connection fail")
            break
        break


if __name__ == "__main__":
    current = time.time()
    reboot = current + 5 * 1800
    j = readData()
    while True:
        thermometer(j)
        if time.time() >= reboot:
            # os.system("sudo reboot")
            break
        time.sleep(10)
