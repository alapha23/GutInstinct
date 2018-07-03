import RPi.GPIO as GPIO
import servo_main as servo
import linear_actuator_module as lin_motor
import linear_actuator_module2 as lin_motor2
import linear_actuator_module3 as lin_motor3
import time

BUTTON_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

angle = 50
servo.rotate(angle)
time.sleep(1)
try:
    while True:
            input_state = GPIO.input(BUTTON_PIN)
            if angle != 50:
                servo.rotate(angle)
            if input_state == False:
                print('Button Pressed')
                angle = 140
                servo.rotate(angle)
                lin_motor.extend(4)
                lin_motor2.extend(4)
                lin_motor3.extend(4)
                lin_motor3.shrink(4)
                lin_motor2.shrink(4)
                lin_motor.shrink(4)
                angle = 50
                servo.rotate(angle)
                time.sleep(1)
                
except KeyboardInterrupt:
    GPIO.cleanup()

