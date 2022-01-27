from ETboard.lib.pin_define import *
from machine import Pin , ADC, PWM
import time

led = Pin(D2)
sensor = ADC(Pin(A1))

def setup() :
    led.init(Pin.OUT)
    sensor.atten(ADC.ATTN_11DB)

def loop() :
    result = 1023 - (sensor.read() / 3)
    print(f'{result : 0.2f}')
    
    pwm2 = PWM(led, 500, int(result))
    
    time.sleep(0.1)

if __name__ == "__main__" :
    setup()
    while True :
        loop()
    