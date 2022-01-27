from ETboard.lib.pin_define import *
from machine import Pin
import time

led_red = Pin(D2)
led_blue = Pin(D3)
led_green = Pin(D4)
led_yellow = Pin(D5)

def setup() :
    led_red.init(Pin.OUT)
    led_blue.init(Pin.OUT)
    led_green.init(Pin.OUT)
    led_yellow.init(Pin.OUT)
    
def loop() :
    led_red.value(HIGH)
    time.sleep(1)
    led_blue.value(HIGH)
    time.sleep(1)
    led_green.value(HIGH)
    time.sleep(1)
    led_yellow.value(HIGH)
    time.sleep(1)

    led_red.value(LOW)
    led_blue.value(LOW)
    led_green.value(LOW)
    led_yellow.value(LOW)
    time.sleep(1)

if __name__ == "__main__" :
    setup()
    while True :
        loop()