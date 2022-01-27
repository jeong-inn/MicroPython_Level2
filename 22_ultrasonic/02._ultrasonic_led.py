import time
from machine import Pin, time_pulse_us
from ETboard.lib.pin_define import *

trig = Pin(D9)
echo = Pin(D8)
led_red = Pin(D2)
led_green = Pin(D4)
led_yellow = Pin(D5)

def setup() :
    trig.init(Pin.OUT)
    echo.init(Pin.IN)
    led_red.init(Pin.OUT)
    led_green.init(Pin.OUT)
    led_yellow.init(Pin.OUT)


def loop() :
    trig.value(LOW)
    echo.value(LOW)
    time.sleep_ms(2)
    trig.value(HIGH)
    time.sleep_ms(2)
    trig.value(LOW)
    
    duration = time_pulse_us(echo, HIGH)
    distance = duration * 17 / 1000
    
    print(f'{distance : .2f}', "cm")
    
    if distance < 10 :
        led_red.value(HIGH)
    else  :
        led_red.value(LOW)
    if (distance >= 10) and (distance < 20) :
        led_yellow.value(HIGH)
    else  :
        led_yellow.value(LOW)
    if distance >= 20 :
        led_green.value(HIGH)
    else  :
        led_green.value(LOW)

if __name__ == "__main__" :
    setup()
    while True :
        loop()

    
    
    