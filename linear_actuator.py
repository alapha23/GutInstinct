import RPi.GPIO as GPIO       
import time                            

PIN = 40

GPIO.setmode(GPIO.BCM)       
GPIO.setup(PIN, GPIO.OUT)             
GPIO.output(PIN, 1)                      
time.sleep(1)
GPIO.cleanup()                         



