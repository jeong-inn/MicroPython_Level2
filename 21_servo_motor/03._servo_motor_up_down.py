import time
from machine import Pin
from ETboard.lib.servo import Servo
from ETboard.lib.pin_define import *

up = Pin(D6)
down = Pin(D9)
servo = Servo(Pin(D2))

def setup() :
    up.init(Pin.IN)
    down.init(Pin.IN)

def loop():
    if up.value() == LOW :
        servo.write_angle(180)
        time.sleep(0.3)
    
    if down.value() == LOW :
        servo.write_angle(0)
        time.sleep(0.3)

if __name__ == "__main__" :
    setup()
    while True :
        loop()
        