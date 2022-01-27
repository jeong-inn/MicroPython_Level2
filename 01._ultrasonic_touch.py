import time
from machine import Pin, time_pulse_us
from ETboard.lib.pin_define import *
from ETboard.lib.servo import Servo

servo = Servo(Pin(D2))
trig = Pin(D9)
echo = Pin(D8)

def setup():
    trig.init(Pin.OUT)
    echo.init(Pin.IN)

def loop() :
    trig.value(LOW)
    echo.value(LOW)
    time.sleep_ms(2)
    trig.value(HIGH)
    time.sleep_ms(2)
    trig.value(LOW)
    
    duration = time_pulse_us(echo, HIGH)
    distance = duration * 17 /1000
    
    if distance <= 20 :
        servo.write_angle(180)
    if distance > 20 :
        servo.write_angle(0)

if __name__ == "__main__" :
    setup()
    while True:
        loop()