from ETboard.lib.pin_define import *
from machine import Pin
import time

button_red = Pin(D6)
button_blue = Pin(D7)
button_green = Pin(D8)
button_yellow = Pin(D9)

led_red = Pin(D2)
led_blue = Pin(D3)
led_green = Pin(D4)
led_yellow = Pin(D5)

button_red_value = 0
button_red_old_value = 1
led_red_status = 0

button_blue_value = 0
button_blue_old_value = 1
led_blue_status = 0

button_green_value = 0
button_green_old_value = 1
led_green_status = 0

button_yellow_value = 0
button_yellow_old_value = 1
led_yellow_status = 0

def setup():
    led_red.init(Pin.OUT)
    led_blue.init(Pin.OUT)
    led_green.init(Pin.OUT)
    led_yellow.init(Pin.OUT)
    
    button_red.init(Pin.IN)
    button_blue.init(Pin.IN)
    button_green.init(Pin.IN)
    button_yellow.init(Pin.IN)

def loop():
    global button_red_value, button_red_old_value, led_red_status
    global button_blue_value, button_blue_old_value, led_blue_status
    global button_green_value, button_green_old_value, led_green_status
    global button_yellow_value, button_yellow_old_value, led_yellow_status
    
    button_red_value = button_red.value()
    button_blue_value = button_blue.value()
    button_green_value = button_green.value()
    button_yellow_value = button_yellow.value()
    
    if button_red_value == LOW and button_red_old_value == HIGH :
        led_red_status = 1 - led_red_status
    button_red_old_value = button_red_value
    if led_red_status == HIGH :
        led_red.value(HIGH)
    else :
        led_red.value(LOW)
    
    if button_blue_value == LOW and button_blue_old_value == HIGH :
        led_blue_status = 1 - led_blue_status
    button_blue_old_value = button_blue_value
    if led_blue_status == HIGH :
        led_blue.value(HIGH)
    else :
        led_blue.value(LOW)
    
    if button_green_value == LOW and button_green_old_value == HIGH :
        led_green_status = 1 - led_green_status
    button_green_old_value = button_green_value
    if led_green_status == HIGH :
        led_green.value(HIGH)
    else :
        led_green.value(LOW)
        
    if button_yellow_value == LOW and button_yellow_old_value == HIGH :
        led_yellow_status = 1 - led_yellow_status
    button_yellow_old_value = button_yellow_value
    if led_yellow_status == HIGH :
        led_yellow.value(HIGH)
    else :
        led_yellow.value(LOW)

if __name__ == "__main__":
    setup()
    while True:
        loop()
