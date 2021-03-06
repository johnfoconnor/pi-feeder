#/usr/bin/python3

from gpiozero import Motor, OutputDevice
from time import sleep
from datetime import datetime as dt
from date_utils import right_now, subtract_days, date_str
from constants import *
import threading
import logging
import notify_email

IS_RUNNING = False
LAST_RUN = subtract_days(right_now(), 1)

class MotorUtil:
	def __init__(self):
		self.enable = OutputDevice(GPIO_PIN_ENABLE)
		self.motor = Motor(GPIO_PIN_FORWARD, GPIO_PIN_BACKWARD)

	def turn_motor_async(self, duration=MOTOR_DEFAULT_DURATION, speed=MOTOR_DEFAULT_SPEED, override=False):
		runner = threading.Thread(target=self.turn_motor, args=(duration,speed,override))
		runner.start()
		return

	def turn_motor(self, duration=MOTOR_DEFAULT_DURATION, speed=MOTOR_DEFAULT_SPEED, override=False):
		"""Turns a Pi motor for the specified duration."""
		global IS_RUNNING
		global LAST_RUN

		if IS_RUNNING:
			logging.debug("Already running!")
			return False

		current_date = right_now()
		if not override:
			if date_str(current_date) == date_str(LAST_RUN):
				logging.debug("Ignoring, already ran at %s " % LAST_RUN)
				return False

		LAST_RUN = current_date
		IS_RUNNING = True
		logging.debug("Running at %s " % date_str(LAST_RUN))

		self.enable.on()
		self.motor.forward(speed)
		sleep(duration)
		self.enable.off()

		IS_RUNNING = False
		logging.debug("Motor going to idle.")
		notify_email.trigger(current_date)
		return True
