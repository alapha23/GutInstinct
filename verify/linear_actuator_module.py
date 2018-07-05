import RPi.GPIO as GPIO       
import time                            

PIN_1 = 15
PIN_2 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_1, GPIO.OUT)             
GPIO.setup(PIN_2, GPIO.OUT)             
try:
    t = 15
   
    # out
    GPIO.output(PIN_2, GPIO.HIGH)                     
    GPIO.output(PIN_2, GPIO.LOW)                      
    GPIO.output(PIN_1, GPIO.HIGH)                     
    time.sleep(t)

    # in

    GPIO.output(PIN_1, GPIO.LOW)                      
    GPIO.output(PIN_2, GPIO.HIGH)                     
    time.sleep(t)
    
        
    #t = 3
    # in
    #GPIO.output(PIN_1, GPIO.LOW)                      
    #GPIO.output(PIN_2, GPIO.HIGH)                     
    #time.sleep(t)
    # out    
    #GPIO.output(PIN_1, GPIO.HIGH)                     
    #GPIO.output(PIN_2, GPIO.LOW)                      
    #time.sleep(t)
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()





