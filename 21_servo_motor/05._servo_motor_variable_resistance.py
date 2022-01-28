import time
from machine import Pin, ADC
from ETboard.lib.servo import Servo
from ETboard.lib.pin_define import *

servo = Servo(Pin(D2))
sensor = ADC(Pin(A0))

def setup() :
    sensor.atten(ADC.ATTN_11DB)
    
def loop() :
    pos = int(sensor.read()/15)
    servo.write_angle(pos)
    print(pos)
    time.sleep(0.02)

if __name__ == "__main__" :
    setup()
    while True :
        loop()