# 📡 Raspberry Pi & Laptop — MQTT Messaging

Simple project that sends MQTT messages from a **Laptop (Ubuntu)** to a **Raspberry Pi 4** running the **Mosquitto** broker, all over a local network.

---

## How It Works

1. The **Raspberry Pi** runs a Mosquitto MQTT broker and listens for messages.
2. The **Laptop** runs a Python script that publishes messages to the broker every 5 seconds.
3. Messages appear in real-time on the Raspberry Pi's terminal.

```
 💻 Laptop (Ubuntu)                     🍓 Raspberry Pi 4
┌─────────────────────┐               ┌─────────────────────┐
│  publisher.py       │  ── MQTT ──▶  │  Mosquitto broker   │
│  sends "Hello..."   │   iot/test    │  mosquitto_sub      │
│  every 5 seconds    │               │  prints messages    │
└─────────────────────┘               └─────────────────────┘
```

---

## Setup

### Raspberry Pi

**1. Connect via SSH from your laptop:**

```bash
ssh pi@192.168.1.8
```

**2. Install Mosquitto broker (run `install_mosquitto.sh`):**

```bash
chmod +x install_mosquitto.sh
./install_mosquitto.sh
```

**3. Start listening for messages (run `subscriber.sh`):**

```bash
chmod +x subscriber.sh
./subscriber.sh
```

Leave this terminal open.

---

### Laptop (Ubuntu)

**1. Create a virtual environment and install paho-mqtt:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install paho-mqtt
```

**2. Run the publisher script:**

```bash
python3 publisher.py
```

---

## The Code

### Raspberry Pi — Install Mosquitto (`install_mosquitto.sh`)

```bash
sudo apt update
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

### Raspberry Pi — Subscriber (`subscriber.sh`)

```bash
mosquitto_sub -h localhost -t "iot/test"
```

### Laptop — Publisher (`publisher.py`)

```python
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
```

> **Note:** Change `192.168.1.8` to your Raspberry Pi's IP address.

---

## Output

**Laptop terminal:**

```
Published: Hello from Laptop to Raspi  →  Topic: iot/test
Published: Hello from Laptop to Raspi  →  Topic: iot/test
Published: Hello from Laptop to Raspi  →  Topic: iot/test
```

**Raspberry Pi terminal (SSH):**

```
Hello from Laptop to Raspi
Hello from Laptop to Raspi
Hello from Laptop to Raspi
```

---

## Project Structure

```
raspi_mqtt_lab/
├── install_mosquitto.sh   # Installs Mosquitto broker (runs on Raspberry Pi)
├── subscriber.sh          # Subscribes to MQTT messages (runs on Raspberry Pi)
├── publisher.py           # Python MQTT publisher (runs on Laptop)
└── README.md
```

