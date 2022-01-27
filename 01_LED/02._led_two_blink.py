from ETboard.lib.pin_define import *
from machine import Pin
import time

led_red = Pin(D2)
led_yellow = Pin(D5)

def setup():
    led_red.init(Pin.OUT)
    led_yellow.init(Pin.OUT)
    
def loop():
    led_red.value(HIGH)
    led_yellow.value(HIGH)
    time.sleep(2)
    
    led_red.value(LOW)
    led_yellow.value(LOW)
    time.sleep(2)
    
if __name__ == "__main__":
    setup()
    while True :
        loop()