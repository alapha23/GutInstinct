import RPi.GPIO as GPIO
import time

PIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
            input_state = GPIO.input(PIN)
            if input_state == False:
                print('Button Pressed')
                time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()

