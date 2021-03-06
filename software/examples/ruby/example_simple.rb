#!/usr/bin/env ruby
# -*- ruby encoding: utf-8 -*-

require 'tinkerforge/ip_connection'
require 'tinkerforge/bricklet_voltage_current'

include Tinkerforge

HOST = 'localhost'
PORT = 4223
UID = 'XYZ' # Change XYZ to the UID of your Voltage/Current Bricklet

ipcon = IPConnection.new # Create IP connection
vc = BrickletVoltageCurrent.new UID, ipcon # Create device object

ipcon.connect HOST, PORT # Connect to brickd
# Don't use device before ipcon is connected

# Get current voltage
voltage = vc.get_voltage
puts "Voltage: #{voltage/1000.0} V"

# Get current current
current = vc.get_current
puts "Current: #{current/1000.0} A"

puts 'Press key to exit'
$stdin.gets
ipcon.disconnect
