#!/usr/bin/python3

import cgi
import cgitb; cgitb.enable()
import json
from sense_hat import SenseHat

sense = SenseHat()

print("Content-Type: application/json\n")

model = {}
temp_model = {}
measurement = {}
measurement["name"] = "pressure"
measurement["value"] = sense.get_pressure()
measurement["unit"] = "hPa"
temp_model["0"] = measurement

measurement= {}
measurement["name"] = "temperature"
measurement["value"] = sense.get_temperature()
measurement["unit"] = "C"
temp_model["1"] = measurement

measurement = {}
measurement["name"] = "humidity"
measurement["value"] = sense.get_humidity()
measurement["unit"] = "%"
temp_model["2"] = measurement

model["sensors"] = temp_model

orientation = sense.get_orientation_degrees()
temp_model = {}

measurement = {}
measurement["name"] = "roll"
measurement["value"] = orientation["roll"]
measurement["unit"] = "degrees"
temp_model["0"] = measurement

measurement = {}
measurement["name"] = "pitch"
measurement["value"] = orientation["pitch"]
measurement["unit"] = "degrees"
temp_model["1"] = measurement

measurement = {}
measurement["name"] = "yaw"
measurement["value"] = orientation["yaw"]
measurement["unit"] = "degrees"
temp_model["2"] = measurement

model["orientation"] = temp_model

temp_model = {}

with open("/home/pi/server/joystick.dat") as f:
        result_joystick = json.load(f)
        measurement = {}
        measurement["name"] = "x"
        measurement["value"] = result_joystick["x"]
        measurement["unit"] = "-"
        temp_model["0"] = measurement
        
        measurement = {}
        measurement["name"] = "y"
        measurement["value"] = result_joystick["y"]
        measurement["unit"] = "-"
        temp_model["1"] = measurement
        
        measurement = {}
        measurement["name"] = "mid_counter"
        measurement["value"] = result_joystick["mid_counter"]
        measurement["unit"] = "-"
        temp_model["2"] = measurement

model["joystick"] = temp_model

print(json.dumps(model))
