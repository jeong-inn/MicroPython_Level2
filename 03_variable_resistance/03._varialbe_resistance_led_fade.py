from ETboard.lib.pin_define import *
from machine import Pin, ADC, PWM
import time

led = Pin(D2)
sensor = ADC(Pin(A0))

def setup():
    sensor.atten(ADC.ATTN_11DB)
    led.init(Pin.OUT)
    

def loop():
    result = sensor.read()
    print(result)
    
    pwm2 = PWM(led, 500, int(result))
    time.sleep(0.1)
    
if __name__ == "__main__" :
    setup()
    while True :
        loop()