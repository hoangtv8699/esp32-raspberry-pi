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
                baudrate=9600,
            )
            read_serial = ser.readline()
            print(read_serial)
            j = json.loads(read_serial.decode("utf-8"))
            return j
        except Exception as e:
            return None
        break


def thermometer(j):
    if j is None:
        print("no data")
        return False
    try:
        # Sending the data to thingspeak
        conn = urllib.request.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s' % (
            j['temp'], j['humidity'], j['light'], j['ec'], j['ph'], j['waterTemp']))
        print(j['temp'], j['humidity'], j['light'], j['ec'], j['ph'], j['waterTemp'])
        # Closing the connection
        conn.close()
        return True
    except Exception as e:
        print(e)
        print("connection fail")
        return False


def writeFile(j):
    try:
        f = open('data.txt', 'a')
        str = '{"temp":%s,"humidity":%s,"light":%s,"ec":%s,"ph":%s,"waterTemp":%s}' % (j['temp'], j['humidity'], j['light'], j['ec'], j['ph'], j['waterTemp'])
        f.write(str + " " + time.ctime())
        f.write('\n')
        print("write success")
    except Exception as e:
        print(e)
        print("write fail")


if __name__ == "__main__":
    current = time.time()
    '''
    j = json.loads('{"temp":12,"humidity":14,"light":11,"ec":1,"ph":13,"waterTemp":1}')
    '''
    while True:
        j = readData()
        re = thermometer(j)
        if (re):
            writeFile(j)
            time.sleep(900)
        else:
            continue
