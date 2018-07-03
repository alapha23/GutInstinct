import RPi.GPIO as GPIO       
import time                            

PIN_1 = 25
PIN_2 = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_1, GPIO.OUT)             
GPIO.setup(PIN_2, GPIO.OUT)             
def extend(t):
    GPIO.output(PIN_1, GPIO.LOW)                      
    GPIO.output(PIN_2, GPIO.HIGH)                     
    #shrink when M+ is lower than M-
    time.sleep(t)

def shrink(t):
    GPIO.output(PIN_1, GPIO.HIGH)                     
    GPIO.output(PIN_2, GPIO.LOW)                      
    time.sleep(t)




