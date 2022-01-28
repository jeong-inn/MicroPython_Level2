import time
from machine import Pin
from ETboard.lib.OLED_U8G2 import *

oled = oled_u8g2()
touch = Pin(D2)

def setup() :
    touch.init(Pin.IN)

def loop() :
    oled.clear()
    oled.setLine(2, " ")
    
    if touch.value() == HIGH :
        oled.clear()
        oled.setLine(2, "touch")
    oled.display()

if __name__ == "__main__":
    setup()
    while True:
        loop()