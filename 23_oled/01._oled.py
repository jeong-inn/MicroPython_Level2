from ETboard.lib.OLED_U8G2 import *
    
oled = oled_u8g2()

def setup() :
    pass

def loop() :
    oled.setLine(2, "jeong-inn!")
    oled.display()

if __name__ == "__main__" :
    setup()
    while True :
        loop()