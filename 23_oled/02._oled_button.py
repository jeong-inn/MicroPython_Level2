from ETboard.lib.OLED_U8G2 import *
from machine import Pin

oled = oled_u8g2()
button_red = Pin(D6)
button_blue = Pin(D7)
button_green = Pin(D8)
button_yellow = Pin(D9)

def setup() :
    button_red.init(Pin.IN)
    button_blue.init(Pin.IN)
    button_green.init(Pin.IN)
    button_yellow.init(Pin.IN)

def loop() :
    oled.clear()
    oled.setLine(2, "Push Button!")
    
    if button_red.value() == LOW :
        oled.clear()
        oled.setLine(2, "red")
     
    if button_blue.value() == LOW :
        oled.clear()
        oled.setLine(2, "blue")
    
    if button_green.value() == LOW :
        oled.clear()
        oled.setLine(2, "green")
    
    if button_yellow.value() == LOW :
        oled.clear()
        oled.setLine(2, "yellow")
    
    oled.display()

if __name__ == "__main__" :
    setup()
    while True :
        loop()