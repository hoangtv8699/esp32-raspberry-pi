import urllib
import time
import random
import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0
key = "3VCJACKUH9UCEOCB"  # Put your API Key here
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % key
def thermometer():
    while True:
        temp = random.randint(1, 10)
        humidity = random.randint(1, 10)
        light = random.randint(1, 10)
        ec = random.randint(1, 10)
        ph = random.randint(1, 10)
        try:
            # Sending the data to thingspeak
            conn = urllib.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s' % (temp, humidity, light, ec, ph))
            print(temp, humidity, light, ec, ph)
            # Closing the connection
            conn.close()
        except:
             break
        break

if __name__ == "__main__":
        while True:
                thermometer()
                time.sleep(30)


