#!/bin/bash
# Install and start Mosquitto broker on Raspberry Pi

sudo apt update
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto

echo "Mosquitto broker is running!"

