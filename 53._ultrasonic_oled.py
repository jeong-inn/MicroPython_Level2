import time
from machine import Pin, time_pulse_us
from ETboard.lib.OLED_U8G2 import *

oled = oled_u8g2()
trig = Pin(D9)
echo = Pin(D8)

def setup() :
    trig.init(Pin.OUT)
    echo.init(Pin.IN)

def loop() :
    trig.value(LOW)
    echo.value(LOW)
    time.sleep_ms(2)
    trig.value(HIGH)
    time.sleep_ms(10)
    trig.value(LOW)
    
    duration = time_pulse_us(echo, HIGH)
    distance = duration * 17 / 1000
    
    if distance > 0 :
        oled.clear()
        oled.setLine(2, "danger!")
    
    if distance > 20 :
        oled.clear()
        oled.setLine(2, "warning!")
    
    if distance > 30 :
        oled.clear()
        oled.setLine(2, "safe!")
    
    oled.display()
    print(distance)
    
if __name__ == "__main__" :
    setup()
    while True :
        loop()