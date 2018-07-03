import wiringpi
import time

PIN = 18

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PIN,  wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
 
delay_period = 0.01
  
def rotate(angle=100):
    wiringpi.pwmWrite(PIN, angle)
    #time.sleep(delay_period*30)

    #for pulse in range(50, 250, 1):
    #    wiringpi.pwmWrite(PIN, pulse)
    #    time.sleep(delay_period)
    #    print(pulse)
    #    for pulse in range(250, 50, -1):
    #             wiringpi.pwmWrite(PIN, pulse)
    #             time.sleep(delay_period)
    #             print(pulse)

def reset():
         wiringpi.pwmWrite(PIN, 0)
         time.sleep(delay_period)
#while True:
#     for pulse in range(50, 250, 1):
#         wiringpi.pwmWrite(PIN, pulse)
#         time.sleep(delay_period)
#         for pulse in range(250, 50, -1):
