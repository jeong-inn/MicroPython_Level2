from ETboard.lib.pin_define import *
from ETboard.lib.pitches import
import time

buzzer = Pin(D6)
previousButtonMillis = 0
melody_note[] = { NOTE_E7, NOTE_E7, 0, NOTE_E7, 0, NOTE_C7, NOTE_E7, 0, NOTE_G7, 0, 0, 0, NOTE_G6, 0, 0, 0, NOTE_C7, 0, 0, NOTE_G6, 0, 0, NOTE_E6, 0, 0, NOTE_A6, 0, NOTE_B6, 0, NOTE_AS6, NOTE_A6, 0, NOTE_G6, NOTE_E7, NOTE_G7, NOTE_A7, 0, NOTE_F7, NOTE_G7, 0, NOTE_E7, 0, NOTE_C7, NOTE_D7, NOTE_B6, 0, 0, NOTE_C7, 0, 0, NOTE_G6, 0, 0, NOTE_E6, 0, 0, NOTE_A6, 0, NOTE_B6, 0, NOTE_AS6, NOTE_A6, 0, NOTE_G6, NOTE_E7, NOTE_G7, NOTE_A7, 0, NOTE_F7, NOTE_G7, 0, NOTE_E7, 0, NOTE_C7, NOTE_D7, NOTE_B6, 0, 0 };
noteDurations[]={ 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, }
melody_num = 0
unsigned long beepTime = 0

def setup() :
    buzzer.init(Pin.OUT)

def loop() :
      if (millis() - beepTime >= 2000/noteDurations[melody_num]) :
            beepTime = millis();
            ledcWrite(0,0); 
            ledcWriteTone(0,melody_note[melody_num]);  
            melody_num++;
            if (melody_num == 50) :
                ledcWrite(0,0); 
                melody_num = 0; 
                beepTime = 0;
    
  
if __name__ == "__main__" :
    setup()
    while True :
        loop()