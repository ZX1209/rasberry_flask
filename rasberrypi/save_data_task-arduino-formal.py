import json
import requests
import serial
import time
import datetime
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

connect=sqlite3.connect('test.db')
cursor = connect.cursor()


arduino = serial.Serial('/dev/ttyACM0',9600,timeout=2);

arduino.write(b'h')
arduino.readall()

def get_sensor_value(s):
    arduino.write(s)
    sensorValue=arduino.readline()
    sensorValue=sensorValue.split()[0]
    return float(sensorValue)



#try and exceptstructure are exception handler
try:
  while 1:
      soil = get_sensor_value(b's')
      light = get_sensor_value(b'l')
      heat = get_sensor_value(b'h')
      knob = get_sensor_value(b'k')
      ispeople = get_sensor_value(b'p')
      t = datetime.datetime.now()
      t=str(t)

      print(t,soil,light,heat,knob,ispeople)
      tmp = (t,light,heat,soil,knob,ispeople)

      try:
          cursor.execute('insert into alldata(time,soil,light,heat,knob,ispeople) values(?,?,?,?,?,?)',tmp)
          connect.commit() 
          logging.debug('saved')
          time.sleep(30)

      except sqlite3.OperationalError :
          logging.debug('locked')
          time.sleep(2)



finally:
    connect.commit()
    connect.close()
    arduino.close();



