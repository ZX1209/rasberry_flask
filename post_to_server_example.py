#! /usr/bin/env python3


import json
import requests
import serial

arduino = serial.Serial('/dev/ttyACM0',115200,timeout=1)

arduino.readline()
arduino.readline()
arduino.readline()
arduino.readline()
arduino.readline()
arduino.readline()

tmp = arduino.readline()
tmp=tmp.decode('utf-8')
tmp_ints=list(map(int,tmp.split(',')))

posts=[
            {'key':'test1',
             'value':tmp_ints[0]
             },
             {'key':'test2',
             'value':tmp_ints[1]
             },
             {'key':'test3',
             'value':tmp_ints[2]
             }
           ]

json_data=json.dumps(posts)

requests.post('http://159.89.155.162:5000/info',data=json_data)



arduino.close()
