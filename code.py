# Write your code here :-)
import board
import digitalio
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

led = digitalio.DigitalInOut(board.A3)
led.direction = digitalio.Direction.OUTPUT

switch = digitalio.DigitalInOut(board.D2)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard()
keyboard_layout = KeyboardLayoutUS(keyboard)

led.value = True

while True:
    time.sleep(0.5)
    if not switch.value:
        led.value = False
        keyboard.press(Keycode.F5)
        keyboard.release_all()
        print("Switch is on!")
        time.sleep(1)
    else:
        led.value = True
        print("Switch is off!")