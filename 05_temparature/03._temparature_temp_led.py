from ETboard.lib.pin_define import *
from machine import Pin, ADC
import time
import math

R1 = 10000
c1 = 1.009249522e-03
c2 = 2.378405444e-04
c3 = 2.019202697e-07

led_red = Pin(D2)
led_blue = Pin(D3)
led_green = Pin(D4)
led_yellow = Pin(D5)

sensor = ADC(Pin(A2))
def setup():
    sensor.atten(ADC.ATTN_11DB)
    led_red.init(Pin.OUT)
    led_blue.init(Pin.OUT)
    led_green.init(Pin.OUT)
    led_yellow.init(Pin.OUT)
 
def loop():
    led_red.value(LOW)
    led_blue.value(LOW)
    led_green.value(LOW)
    led_yellow.value(LOW)

    Vo = sensor.read()
    R2 = R1 * (4095.0 / Vo - 1.0)
    logR2 = math.log(R2)
    T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2))
    Tc = T - 273.15
    
    if (Tc < 10) :
        led_blue.value(HIGH)
        print("blue on")
    
    if (Tc >= 10) and (Tc < 20) :
        led_green.value(HIGH)
        print("green on")
    
    if (Tc >= 20) and (Tc < 30) :
        led_yellow.value(HIGH)
        print("yellow on")
    
    if (Tc >= 30) :
        led_red.value(HIGH)
        print("red on")
           
    print(f'{Tc:0.2f}', "°C")
    
    time.sleep(0.1)

if __name__ == "__main__":
    setup()
    while True :
        loop()