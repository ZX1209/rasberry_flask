#! /usr/bin/env python3

import serial

arduino = serial.Serial('/dev/ttyACM0',115200,timeout=1)

try:
    while 1:
        print(arduino.readline())
except:
    arduino.close()

