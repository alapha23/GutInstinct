import wiringpi
import time

SERVO_PIN = 18

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(SERVO_PIN,  wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(1000)
 
angle = 50  
wiringpi.pwmWrite(SERVO_PIN, angle)
time.sleep(1)
angle = 140
wiringpi.pwmWrite(SERVO_PIN, angle)
