import time
from machine import Pin
from ETboard.lib.servo import Servo
from ETboard.lib.pin_define import *

up = Pin(D6)
down = Pin(D9)
servo = Servo(Pin(D2))
pos = 0

def setup() :
    up.init(Pin.IN)
    down.init(Pin.IN)

def loop() :
    global pos
    
    if up.value() == LOW :
        pos += 1
        if pos >180 :
            pos = 180
        servo.write_angle(pos)
        time.sleep(0.01)
    
    if down.value() == LOW :
        pos -= 1
        if pos< 0 :
            pos = 0
        servo.write_angle(pos)
        time.sleep(0.01)

if __name__ == "__main__" :
    setup()
    while True :
        loop()
        
        