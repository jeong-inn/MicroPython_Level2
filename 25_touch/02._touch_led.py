import time
from machine import Pin
from ETboard.lib.pin_define import *

led_red = Pin(D2)
led_blue = Pin(D3)
led_green = Pin(D4)
led_yellow = Pin(D5)
touch = Pin(D6)

def setup() :
    led_red.init(Pin.OUT)
    led_blue.init(Pin.OUT)
    led_green.init(Pin.OUT)
    led_yellow.init(Pin.OUT)
    touch.init(Pin.IN)
    
def loop():
    led_red.value(LOW)
    led_blue.value(LOW)
    led_green.value(LOW)
    led_yellow.value(LOW)
    
    if touch.value() == HIGH :
        led_red.value(HIGH)
        led_blue.value(HIGH)
        led_green.value(HIGH)
        led_yellow.value(HIGH)
    time.sleep(0.1)

if __name__ == "__main__" :
    setup()
    while True :
        loop()

