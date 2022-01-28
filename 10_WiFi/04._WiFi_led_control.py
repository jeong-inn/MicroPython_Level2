import time
from machine import Pin, ADC
import ETboard.lib.WiFi as WiFi
from ETboard.lib.pin_define import *

led = Pin(D2)
ssid = "ssid"
password = "password"
server = WiFi.WebServer(80)
html_page = "<font size=16>Click <a href=\"/red_led_on\"> red On </a> to turn On LED<br></font>"\
            "<font size=16>Click <a href=\"/red_led_off\"> red Off</a> to turn Off LED<br></font>"


def handle_root() :
    led.value(HIGH)
    print("root call")
    server.send(200, "text/html", html_page)
    led.value(LOW)

def handle_d2on() :
    print("D2 On call")
    led.value(HIGH)
    server.send(200, "text/html", html_page)

def handle_d2off():
    print("D2 Off call")
    led.value(LOW)
    server.send(200, "text/html", html_page)

def setup() :
    led.init(Pin.OUT)
    WiFi.begin(ssid, password)
    
    while WiFi.status() != WiFi.WL_CONNECTED :
        time.sleep(0.5)
        print(".")
    
    print("")
    print("WiFi connected")
    print("IP address : ")
    print(WiFi.localIP())
    
    server.on("/", handle_root)
    server.on("/red_led_on", handle_d2on)
    server.on("/red_led_off", handle_d2off)
    server.begin()
    
def loop() :
    server.handleClient()
    print("loop run...")
    time.sleep(0.02)

if __name__ == "__main__" :
    setup()
    while True :
        loop()