from ETboard.lib.pin_define import *
import time
from machine import Pin

buzzer = Pin(D2)
count = 0

def setup():
    buzzer.init(Pin.OUT)

def loop() :
    global count
    while count < 1 :
        for i in range(80) :
            buzzer.value(HIGH)
            time.sleep(0.001)
            buzzer.value(LOW)
            time.sleep(0.001)
        count = 1

if __name__ == "__main__" :
    setup()
    while True :
        loop()