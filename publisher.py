"""
MQTT Publisher — runs on Laptop (Ubuntu)
Publishes messages to the Mosquitto broker on the Raspberry Pi.

Usage:
    source venv/bin/activate
    python3 publisher.py
"""

import paho.mqtt.client as mqtt
import time

MQTT_BROKER = "192.168.1.8"   # Raspberry Pi IP address
MQTT_TOPIC  = "iot/test"

client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

while True:
    message = "Hello from Laptop to Raspi"
    client.publish(MQTT_TOPIC, message)
    print(f"Published: {message}  →  Topic: {MQTT_TOPIC}")
    time.sleep(5)
