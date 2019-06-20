import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

for i in range (50):
    GPIO.output(7,true)
    time.sleep(1)
    GPOI.output(7,false)
    time.sleep(1)
    
GPIO.cleanup()
