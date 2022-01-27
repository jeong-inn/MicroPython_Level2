from ETboard.lib.pin_define import *
from machine import Pin, ADC
import time

led_red = Pin(D2)
led_blue = Pin(D3)
led_green = Pin(D4)
led_yellow = Pin(D5)
sensor = ADC(Pin(A0))

def setup():
    sensor.atten(ADC.ATTN_11DB)
    led_red.init(Pin.OUT)
    led_blue.init(Pin.OUT)
    led_green.init(Pin.OUT)
    led_yellow.init(Pin.OUT)

def loop():
    result = sensor.read()
    led_red.value(LOW)
    led_blue.value(LOW)
    led_green.value(LOW)
    led_yellow.value(LOW)

    if result >500 :
        led_red.value(HIGH)
    
    if result >1000 :
        led_blue.value(HIGH)
        
    if result >1500 :
        led_green.value(HIGH)
        
    if result >2000 :
        led_yellow.value(HIGH)
if __name__ == "__main__" :
    setup()
    while True :
        loop()
    

