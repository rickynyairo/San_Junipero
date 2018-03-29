#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT

#Pin Setup
ldr=24
fan_forward = 20
soil_moisture = 21
water_pump = 16
vent_servo = 02
vent_angle = 90

#GPIO SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_forward, GPIO.OUT)
GPIO.setup(water_pump, GPIO.OUT)
GPIO.setup(soil_moisture, GPIO.IN)
GPIO.setup(vent_servo, GPIO.OUT)

#infinite loop
def main_func():

	humidity, temperature = Adafruit_DHT.read_retry(11,4)

	print "Temperature: " + str(temperature) + " °C"
	print "Humidity: " + str(humidity) + " %"
	print "LDR: " + str(ldr_reading())
	soil_moisture_state = GPIO.input(soil_moisture)

	if (soil_moisture_state == 1):
		print "The soil is dry"
		GPIO.output(water_pump, GPIO.HIGH)
		sleep(3)
	else:
		print "The soil is wet"
		GPIO.output(water_pump, GPIO.LOW)

	if (temperature > 29):
		print "High Temperature, starting fan"
		GPIO.output(fan_forward, GPIO.HIGH)

		open_vent(vent_angle)

	sleep(2)

#function for the ldr
def ldr_reading():
	count=0

	GPIO.setup(ldr, GPIO.OUT)
	GPIO.output(ldr, GPIO.LOW)
	time.sleep(1)

	GPIO.setup(ldr,GPIO.IN)

	while(GPIO.input(ldr)==GPIO.LOW):
		count += 1

	return count

#function to open vent
def open_vent(angle = vent_angle):
	#setup pwm on servo pin
	pwm = GPIO.PWM(vent_servo, 50)
	
	#start with 0 duty cycle
	pwm.start(0)

	#Calculate duty cycle
	duty = (angle / 18) + 2
	GPIO.output(vent_servo, True)

	pwm.ChangeDutyCycle(duty)
	sleep(1)

	GPIO.output(vent_servo, False)
	pwm.ChangeDutyCycle(0)

try:
	while True:

		start = int(raw_input("Enter Angle? (0-90)"))

		open_vent(start)

		sleep(2)

except KeyboardInterrupt:
	GPIO.cleanup()



