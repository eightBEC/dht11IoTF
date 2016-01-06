import RPi.GPIO as GPIO
import time
import os, json
import ibmiotf.device
import uuid
import dht11



client = None


try:
    options = ibmiotf.device.ParseConfigFile("/home/pi/device.cfg")
    print options
    client = ibmiotf.device.Client(options)
    client.connect()
    
    while True:
    humidityTemp = dht11.getHumTemp()
	if(len(humidityTemp) > 1):
		myData = {'d':{'humidity' : int(humidityTemp[0]), 'temperature': int(humidityTemp[1])}}
		print myData
		client.publishEvent("status","json",myData)
        time.sleep(60)

except ibmiotf.ConnectionException  as e:
    print e
