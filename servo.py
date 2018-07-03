import RPi.GPIO as GPIO
import time
servoPIN = 15
speed = 50
degree = 11000
#def rotate(speed=50, degree=11000):
if True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, speed) # GPIO 14 for PWM with 50Hz
    # frequency here means speed of rotating
    
    p.start(5) # Initialization
    try:
        for k in range(2000):
            dc = 5            
            for i in range(4):
                dc = dc + 2.5
                p.ChangeDutyCycle(dc)
            for i in range(4):
                dc = dc - 2.5
                p.ChangeDutyCycle(dc)

    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
    finally:
        GPIO.cleanup()

