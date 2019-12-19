import serial, time
import json


while 1:
    j = json.loads('{ "temp" : "12", "hunmidity" : "12", "light" : "12", "ec" : "12", "ph" : "12", "waterTemp" : "14"}')
    print(j['temp'])