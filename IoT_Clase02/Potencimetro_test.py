from machine import Pin,ADC
from time import sleep

volume=ADC(Pin(34))


while True:
    x=volume.read()
    print(x)
    sleep(1)