from ETboard.lib.OLED_U8G2 import *
from machine import Pin, ADC
import time

sensor = ADC(Pin(A1))
oled = oled_u8g2()

def setup() :
    sensor.atten(ADC.ATTN_11DB)
    
def loop() :
    result = sensor.read()
    
    if result >= 700 :
        oled.clear()
        oled.setLine(2, "MORNING!")
    
    if result < 700 :
        oled.clear()
        oled.setLine(2, "NIGHT!")
    oled.display()
    
if __name__ == "__main__" :
    setup()
    while True :
        loop()