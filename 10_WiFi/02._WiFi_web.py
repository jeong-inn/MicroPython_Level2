from ETboard.lib.pin_define import *
import ETboard.lib.WiFi as WiFi
from machine import Pin
import time

ssid = "ssid"
password = "password"
server = WiFi.WebServer(80)
led = Pin(D2)

def handle_root() :
    led.value(HIGH)
    server.send(200, "text/plain", "hello jeong-inn! __ {}".format(time.time()))
    led.value(LOW)

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
    server.begin()

def loop() :
    server.handleClient()
    print("loop run...")
    time.sleep(20)
    
if __name__ == "__main__" :
    setup()
    while True :
        loop()