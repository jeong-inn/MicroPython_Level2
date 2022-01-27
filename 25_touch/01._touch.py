from ETboard.lib.pin_define import *
from machine import Pin
import time

touch = Pin(D2)

def setup() :
    touch.init(Pin.IN)

def loop() :
    result = touch.value()
    print(result)
    time.sleep(0.1)

if __name__ == "__main__" :
    setup()
    while True :
        loop()