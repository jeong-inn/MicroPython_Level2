import time
from machine import Pin
from ETboard.lib.pin_define import *

led_red = Pin(D2)
led_blue = Pin(D3)

def setup() :
    led_red.init(Pin.OUT)
    led_blue.init(Pin.OUT)
    
def loop() :
    led_red.value(HIGH)
    led_blue.value(LOW)
    time.sleep(5)
    
    led_red.value(LOW)
    led_blue.value(LOW)
    time.sleep(5)
    
    led_red.value(HIGH)
    led_blue.value(HIGH)
    time.sleep(5)
    
    led_red.value(LOW)
    led_blue.value(LOW)
    time.sleep(5)


if __name__ == "__main__" :
    setup()
    while True :
        loop()