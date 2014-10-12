import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
i= 0

while i<10:
	GPIO.output(RED_LED, False)
	GPIO.output(GREEN_LED, True)
	time.sleep(1)
	GPIO.output(GREEN_LED, False)
	GPIO.output(RED_LED, True)
	i=i+1
