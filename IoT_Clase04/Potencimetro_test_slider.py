from machine import Pin,ADC,PWM
from time import sleep

volume=ADC(Pin(13))
volume.atten(ADC.ATTN_11DB)

led=PWM(Pin(2),Pin.OUT)
led.freq(1000)

while 1:
    valor=volume.read()
    nuevovalor=int(valor/4)
    print(valor)
    led.duty(nuevovalor)
    sleep(0.5)