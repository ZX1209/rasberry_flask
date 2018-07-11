#! /usr/bin/env python3

import json
import requests
import serial
import time




arduino = serial.Serial('/dev/ttyACM0', 9600,timeout=1);   #open named port at 9600,1s timeot

#try and exceptstructure are exception handler
try:
  while 1:
    tmp_ints = [0,0,0,0]
    arduino.write(b'h')
    sensorValue=arduino.readline()
    sensorValue=sensorValue.decode('utf-8')
    tmp_ints[0]=int(sensorValue)

    arduino.write(b's')
    sensorValue=arduino.readline()
    sensorValue=sensorValue.decode('utf-8')
    tmp_ints[1]=int(sensorValue)

    arduino.write(b'l')
    sensorValue=arduino.readline()
    sensorValue=sensorValue.decode('utf-8')
    tmp_ints[2]=int(sensorValue)

    arduino.write(b'k')
    sensorValue=arduino.readline()    
    sensorValue=sensorValue.decode('utf-8')
    tmp_ints[3]=int(sensorValue)

    posts=[
        {'key':'温度',
         'value':tmp_ints[0]
         },
         {'key':'湿度',
         'value':tmp_ints[1]
         },
         {'key':'光照',
         'value':tmp_ints[2]
         },
         {'key':'旋钮',
         'value':tmp_ints[2]
         }
        ]

    json_data=json.dumps(posts)

    requests.post('http://159.89.155.162:5000/info',data=json_data)

    time.delay(60);

except:
  arduino.close();



