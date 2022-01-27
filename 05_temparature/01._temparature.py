from ETboard.lib.pin_define import *
from machine import Pin, ADC
import time
import math

sensor = ADC(Pin(A2))

def setup():
    sensor.atten(ADC.ATTN_11DB)
 
def loop():
    result = sensor.read()    
    print(result)
    
    time.sleep(0.1)

if __name__ == "__main__":
    setup()
    while True :
        loop()