from gpiozero import LED
import time

light = LED(14)

def toggle_lights(state):
    print(state)
    if state == "off":
        light.off()
    elif state == 'on':
        light.on()