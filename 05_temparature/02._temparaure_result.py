from ETboard.lib.pin_define import *
from machine import Pin, ADC
import time
import math

R1 = 10000
c1 = 1.009249522e-03
c2 = 2.378405444e-04
c3 = 2.019202697e-07

sensor = ADC(Pin(A2))
def setup():
    sensor.atten(ADC.ATTN_11DB)
 
def loop():
    Vo = sensor.read()
    R2 = R1 * (4095.0 / Vo - 1.0)
    logR2 = math.log(R2)
    T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2))
    Tc = T - 273.15
       
    print(Tc, "°C")
    
    time.sleep(0.1)

if __name__ == "__main__":
    setup()
    while True :
        loop()