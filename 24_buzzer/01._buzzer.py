from ETboard.lib.pin_define import *
import time
from machine import Pin

buzzer = Pin(D2)

def setup():
    buzzer.init(Pin.OUT)

def loop() :
    buzzer.value(HIGH)
    time.sleep(0.001)
    buzzer.value(LOW)
    time.sleep(0.001)

if __name__ == "__main__" :
    setup()
    while True :
        loop()