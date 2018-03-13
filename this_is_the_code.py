#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

#GPIO SETUP
fan_forward = 20
soil_moisture = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_forward, GPIO.OUT)
GPIO.setup(soil_moisture, GPIO.IN)
#infinite loop
while True:
	print "Hello world"

	soil_moisture_state = GPIO.input(soil_moisture)
	choice = raw_input("Start the fan? ")
	if (int(choice) == 1):
		print "Fan on"
		GPIO.output(channel, GPIO.HIGH)
	else:
		print "Fan off"
		GPIO.output(channel, GPIO.LOW)

	sleep(7)


