from ETboard.lib.pin_define import *
from machine import Pin
import time

led_red = Pin(D2)

def setup() :
    led_red.init(Pin.OUT)

def loop() :
    led_red.value(HIGH)
    time.sleep(2)
    
    led_red.value(LOW)
    time.sleep(2)

if __name__ == "__main__" :
    setup()
    while True :
        loop()