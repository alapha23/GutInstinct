import RPi.GPIO as GPIO       
import time                            

PIN_1 = 15
PIN_2 = 23
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_1, GPIO.OUT)             
    GPIO.setup(PIN_2, GPIO.OUT)             
    if True:
        GPIO.output(PIN_1, GPIO.LOW)                      
        GPIO.output(PIN_2, GPIO.HIGH)                     
        #shrink when M+ is lower than M-
        time.sleep(3)
        GPIO.output(PIN_2, GPIO.LOW)                      
        GPIO.output(PIN_1, GPIO.HIGH)                     
        time.sleep(8)
    GPIO.cleanup()                         

except KeyboardInterrupt:
    GPIO.cleanup()                         


