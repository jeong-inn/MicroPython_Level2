import ETboard.lib.WiFi as WiFi
import time

ssid = "ssid"
password = "password"

def setup() :
    WiFi.begin(ssid, password)
    while WiFi.status() != WiFi.WL_CONNECTED :
        time.sleep(0.5)
        print(".")
    
    print("")
    print("WiFi connected")
    print("IP address : ")
    print(WiFi.localIP())

def loop() :
    pass
if __name__ == "__main__" :
    setup()
    while True :
        loop()