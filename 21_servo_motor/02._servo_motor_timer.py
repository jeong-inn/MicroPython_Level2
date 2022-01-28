import time
from ETboard.lib.pin_define import *
from ETboard.lib.servo import Servo
from machine import Pin

servo = Servo(Pin(D2))

def setup() :
    pass

def loop():
    servo.write_angle(180)
    time.sleep(2)
    
    servo.write_angle(0)
    time.sleep(2)
    
if __name__ == "__main__" :
    setup()
    while True :
        loop()