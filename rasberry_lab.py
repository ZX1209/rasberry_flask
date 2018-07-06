#!/usr/bin/env python3

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('import error')

#
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.IN)


