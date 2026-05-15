#!/bin/bash
# Subscribe to MQTT messages on the local Mosquitto broker

mosquitto_sub -h localhost -t "iot/test"

