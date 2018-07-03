import servo_main as servo
import time

# limit of angle is 50 ~ 250

angle = 50
servo.rotate(angle)
time.sleep(1)
angle = 140
servo.rotate(angle)
time.sleep(3)

angle = 50
servo.rotate(angle)
time.sleep(1)







#servo.reset()
