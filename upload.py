import random
import serial
import time
import urllib.request
import os
import json

#



key = '3VCJACKUH9UCEOCB'  # Put your API Key here
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % key


def readData():
    while True:
        try:
            ser = serial.Serial(
     port='/dev/ttyUSB0',
     baudrate = 9600,
)
            read_serial = ser.readline()
            print(read_serial)
            j = json.loads(read_serial.decode("utf-8"))
            return j
        except Exception as e:
            return None
        break


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
    '''
    j = json.loads('{"temp":12,"humidity":14,"light":11,"ec":1,"ph":13,"waterTemp":1}')
    '''
    time.sleep(30)
    reboot = current + 5 * 1800
    while True:
        j = readData()
        thermometer(j)
        '''
        if time.time() >= reboot:
            os.system("sudo reboot")
            break
        '''
        time.sleep(900)
