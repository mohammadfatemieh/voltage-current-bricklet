#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_voltage_current import VoltageCurrent

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    vc = VoltageCurrent(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current voltage (unit is mV)
    voltage = vc.get_voltage()
    print('Voltage: ' + str(voltage/1000.0) + ' V')

    # Get current current (unit is mA)
    current = vc.get_current()
    print('Current: ' + str(current/1000.0) + ' A')

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.disconnect()
