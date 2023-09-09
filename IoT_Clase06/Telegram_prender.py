from machine import Pin, ADC, PWM
import network
import socket
import telegram

ssid ='IUEINALAMBRICA'
pw =''

led= Pin(2,Pin.OUT)

WLAN = network.WLAN(network.STA_IF)
WLAN.active(True)
WLAN.connect(ssid, pw)

while not WLAN.isconnected():
    print("Conectando...")

estado = WLAN.ifconfig()
print(estado)

Token='6156827043:AAHT7sVKnN79H2JPr46zRCohiHFnkTWBcWg'
    
MiID='6270369608'

def respuesta(message):
    print(message)
    bot.send(message['message']['chat']['id'],'pong')
    
def mensaje_leido(message):
    if message['message']['text']=='on':
        led.on()
        bot.send(MiID,"Se prendió")
    else:
        led.off()
 
bot = telegram.ubot(Token)
bot.register('/ping',respuesta)

bot.set_default_handler(mensaje_leido)

print('Hola')
bot.send(MiID,"Solo debías seguir el maldito tren CJ")
bot.listen()





    