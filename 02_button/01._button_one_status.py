from ETboard.lib.pin_define import *
from machine import Pin
import time

button = Pin(D6)

def setup() :
    button.init(Pin.IN)

def loop() :
    if button.value() == LOW :
        print("버튼이 눌림")
    else :
        print("버튼이 눌리지 않음")
    time.sleep(0.1)

if __name__ == "__main__":
    setup()
    while True :
        loop()