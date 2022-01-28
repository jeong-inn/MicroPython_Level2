import time
from machine import Pin, time_pulse_us
from ETboard.lib.pin_define import *

trig = Pin(D9)
echo = Pin(D8)
buzzer = Pin(D2)

def setup() :
    trig.init(Pin.OUT)
    echo.init(Pin.IN)
    buzzer.init(Pin.OUT)

def loop() :
    trig.value(LOW)
    echo.value(LOW)
    time.sleep_ms(2)
    trig.value(HIGH)
    time.sleep_ms(2)
    trig.value(LOW)
    
    duration = time_pulse_us(echo, HIGH)
    distance = duration * 17 / 1000
    
    print(f'{distance : .2f}', "cm")
    time.sleep_ms(100)
    
    if distance < 10 :
        for i in range(80):
            buzzer.value(HIGH)
            time.sleep(0.001)
            buzzer.value(LOW)
            time.sleep(0.001)

if __name__ == "__main__" :
    setup()
    while True :
        loop()