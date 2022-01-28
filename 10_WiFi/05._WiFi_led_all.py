import time
from machine import Pin, ADC
import ETboard.lib.WiFi as WiFi
from ETboard.lib.pin_define import *

ssid = "ssid"
password = "password"

server = WiFi.WebServer(80)
led_red = Pin(D2)
led_blue = Pin(D3)
led_green = Pin(D4)
led_yellow = Pin(D5)

html_page = "<font size=16>Click <a href=\"/red_led_on\"> red On </a> to turn On LED<br></font>"\
            "<font size=16>Click <a href=\"/red_led_off\"> red Off</a> to turn Off LED<br></font>"\
            "<font size=16>Click <a href=\"/blue_led_on\"> blue On </a> to turn On LED<br></font>"\
            "<font size=16>Click <a href=\"/blue_led_off\"> blue Off</a> to turn Off LED<br></font>"\
            "<font size=16>Click <a href=\"/green_led_on\"> green On </a> to turn On LED<br></font>"\
            "<font size=16>Click <a href=\"/green_led_off\"> green Off</a> to turn Off LED<br></font>"\
            "<font size=16>Click <a href=\"/yellow_led_on\"> yellow On </a> to turn On LED<br></font>"\
            "<font size=16>Click <a href=\"/yellow_led_off\"> yellow Off</a> to turn Off LED<br></font>"
 


def handle_root() :
    led_red.value(HIGH)
    print("root call!")
    server.send(200, "text/html", html_page)
    led_red.value(LOW)

def handle_d2on() :
    print("D2 On call!")
    led_red.value(HIGH)
    server.send(200, "text/html", html_page)

def handle_d2off() :
    print("D2 Off call!")
    led_red.value(LOW)
    server.send(200, "text/html", html_page)

def handle_d3on() :
    print("D3 On call!")
    led_blue.value(HIGH)
    server.send(200, "text/html", html_page)

def handle_d3off() :
    print("D3 Off call!")
    led_blue.value(LOW)
    server.send(200, "text/html", html_page)

def handle_d4on() :
    print("D4 On call!")
    led_green.value(HIGH)
    server.send(200, "text/html", html_page)

def handle_d4off() :
    print("D4 Off call!")
    led_green.value(LOW)
    server.send(200, "text/html", html_page)

def handle_d5on() :
    print("D5 On call!")
    led_yellow.value(HIGH)
    server.send(200, "text/html", html_page)

def handle_d5off() :
    print("D5 Off call!")
    led_yellow.value(LOW)
    server.send(200, "text/html", html_page)

def setup() :
    led_red.init(Pin.OUT)
    led_blue.init(Pin.OUT)
    led_green.init(Pin.OUT)
    led_yellow.init(Pin.OUT)
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
    server.on("/blue_led_on", handle_d3on)
    server.on("/blue_led_off", handle_d3off)
    server.on("/green_led_on", handle_d4on)
    server.on("/green_led_off", handle_d4off)
    server.on("/yellow_led_on", handle_d5on)
    server.on("/yellow_led_off", handle_d5off)
    server.begin()
    
def loop():
    server.handleClient()
    print("loop run...")
    time.sleep(0.02)

if __name__ == "__main__":
    setup()
    while True:
        loop()

