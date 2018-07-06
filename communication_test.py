#! /usr/bin/env python3
import serial    #import serial module

ser = serial.Serial('/dev/ttyACM0', 115200,timeout=1);   #open named port at 9600,1s timeot

#try and exceptstructure are exception handler
try:
  while 1:
    ser.write('s');#writ a string to port
    response = ser.readall();#read a string from port
    print(response);
except:
  ser.close();
