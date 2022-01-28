import time
from machine import Pin, ADC
from ETboard.lib.pin_define import *
import ETboard.lib.WiFi as WiFi

ssid = "ssid"
password = "password"
server = WiFi.WebServer(80)
led = Pin(D2)
sensor = ADC(Pin(A0))

def handle_root() :
    led.value(HIGH)
    print("root call")
    server.send(200, "text/plain", "jeong-inn! __ {}".format(time.time()))
    led.value(LOW)

def handle_a0() :
    result = sensor.read()
    send_data = "variable resistance : "
    send_data = send_data + str(result)
    print("A0 call")
    server.send(200, "text/plain", send_data)

def setup() :
    led.init(Pin.OUT)
    sensor.atten(ADC.ATTN_11DB)
    WiFi.begin(ssid, password)
    
    while WiFi.status() != WiFi.WL_CONNECTED :
        time.sleep(0.5)
        print(".")
    
    print("")
    print("WiFi connected")
    print("IP address : ")
    print(WiFi.localIP())
    
    server.on("/", handle_root)
    server.on("/read_a0", handle_a0)
    server.begin()

def loop() :
    server.handleClient()
    print("loop run")
    time.sleep(0.02)

if __name__ == "__main__" :
    setup()
    while True :
        loop()