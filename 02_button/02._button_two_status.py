from ETboard.lib.pin_define import *
from machine import Pin
import time

button_red = Pin(D6)
button_blue = Pin(D7)

def setup() :
    button_red.init(Pin.IN)
    button_blue.init(Pin.IN)
    
def loop() :
    if button_red.value() == LOW :
        print("빨강 버튼이 눌림")

    if button_blue.value() == LOW :
        print("파랑  버튼이 눌림")

    time.sleep(0.1)
    
if __name__ == "__main__" :
    setup()
    while True :
        loop()