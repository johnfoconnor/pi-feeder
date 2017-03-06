#/usr/bin/python3
"""This class will cleanup Pi GPIO references if needed. Not used by this program, should be run manually."""

import RPi.GPIO as GPIO
from time import sleep
from constants import *

GPIO.setmode(GPIO.BCM)

Motor1A = GPIO_PIN_ENABLE
Motor1B = GPIO_PIN_FORWARD
Motor1E = GPIO_PIN_BACKWARD

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

GPIO.output(Motor1A, GPIO.LOW)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1E, GPIO.LOW)

GPIO.cleanup()
