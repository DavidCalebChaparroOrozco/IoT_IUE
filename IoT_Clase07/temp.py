from machine import Pin
from time import sleep
import dht
from umqtt.robust import MQTTClient
import network

# Default token: BBFF-bq8zD9250M0yTYLOZDhyaRzNS9vNfC
# Api Key: BBFF-12d715920f6a9e3e7a6674b3c7ed1412a12

Token = "BBFF-bq8zD9250M0yTYLOZDhyaRzNS9vNfC"
ClienteID = "CJ"
Servidor = "industrial.api.ubidots.com"
puerto = 1883

usuario = Token
contrasena = Token


ssid = "Redmi Note 10 Pro"
pw = "chalo1234"

WLAN = network.WLAN(network.STA_IF)
WLAN.active(True)
WLAN.connect(ssid, pw)

while not WLAN.isconnected():
    print("Conectando...")

estado = WLAN.ifconfig()
print(estado)

cliente = MQTTClient("ClientID", Servidor,puerto, usuario, contrasena)
cliente.connect()

Sensor = dht.DHT11(Pin(15))

while True:
    try:
        sleep(2)
        Sensor.measure()
        Temp = Sensor.temperature()
        print("La temperatura es: ", Temp)

        Humedad = Sensor.humidity()
        print("La Humedad es: ",Humedad)
        
        
        msg1 = b'{"Temperatura":{"value": %s}}' %(Temp)
        msg2 = b'{"Humedad":{"value": %s}}' %(Humedad)
        #Publicar el dato
        cliente.publish(b'/v1.6/devices/esp32CJ',msg1)
        cliente.publish(b'/v1.6/devices/esp32CJ',msg2)
        print(msg1)
        print(msg2)
        
        
    except OSError as e:
        print("Que paso amiguito, no puedo leer nada")