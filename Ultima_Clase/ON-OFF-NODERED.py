from machine import Pin
from umqtt import MQTTClient
import ubinascii
import machine
import micropython
import time
import network
import dht
# Configuración del broker MQTT
broker_address = "broker.mqtt.cool"
port = 1883
topic = "topic/esp32/caleb"
led = Pin(2, Pin.OUT)

ssid = "Redmi Juan"
pw = "87654321"

WLAN = network.WLAN(network.STA_IF)
WLAN.active(True)
WLAN.connect(ssid, pw)

while not WLAN.isconnected():
    print("Conectando...")

estado = WLAN.ifconfig()
print(estado)

def sub_cb(topic, msg):
    print((topic, msg))
    if msg == b'on':
        led.on()
    elif msg == b'off':
        led.off()

def on_message(topic, msg):
    print(f"Nuevo mensaje en el tópico {topic}: {msg.decode()}")

# Configuración del cliente MQTT
client_id = ubinascii.hexlify(machine.unique_id())
cliente = MQTTClient(client_id, broker_address, port)
cliente.set_callback(sub_cb)

# Conexión al broker
cliente.connect()

# Suscripción al tópico
cliente.subscribe(topic)

# Bucle principal para mantener la conexión y procesar mensajes
try:
    while True:
        cliente.check_msg()
        time.sleep(1)
except KeyboardInterrupt:
    print("Desconectando...")
    cliente.disconnect()