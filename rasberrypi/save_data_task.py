import json
import requests
import serial
import time
import datetime
import sqlite3
import logging

logging.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',level=logging.DEBUG)

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
      t = datetime.datetime.now()
      t=str(t)

      print(t,soil,light,heat)
      tmp = (t,light,heat,soil)

      try:
          cursor.execute('insert into test(time,l,h,s) values(?,?,?,?)',tmp)
          connect.commit()
      except sqlite3.OperationalError :
          logging.debug('locked')
          time.sleep(2)


      logging.debug('saved')

      time.sleep(10)
      

finally:
    connect.commit()
    connect.close()
    arduino.close();



