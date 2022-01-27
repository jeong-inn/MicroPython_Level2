from ETboard.lib.pin_define import *
from ETboard.lib.servo import Servo
from machine import Pin
import time

servo = Servo(Pin(D2))

def setup() :
    pass
def loop() :
    pos = 0
    
    for x in range (180) :
        servo.write_angle(pos)
        pos += 1
        time.sleep(0.01)
    
    for x in range (0) :
        servo.write_angle(pos)
        pos -= 1
        time.sleep(0.01)

if __name__ == "__main__" :
    setup()
    while True:
        loop()