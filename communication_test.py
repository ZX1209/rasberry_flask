#! /usr/bin/env python3
import serial    #import serial module

ser = serial.Serial('/dev/ttyACM0', 9600,timeout=2);   #open named port at 9600,1s timeot

#try and exceptstructure are exception handler
try:
  while 1:
    ser.write(b's');#writ a string to port
    response = ser.readline();#read a string from port
    print(response);
except:
  ser.close();
