dht11IoTF
=========
Temperature and Humidity IoT Sample
===================================
This repository contains sample code for measuring temperature and humidity on the Raspberry Pi model B+.

Installation
============
Clone this repository to your RPi and create a configuration file /home/pi/device.cfg containing your IBM Bluemix IoT Foundation configuration
```
[device]
org=$YourOrgId
type=$DeviceType
id=$DeviceId
auth-method=token
authKey=$authKey
auth-token=$authToken
```

Content
=======
By running the following command on your RPi, every 60 seconds an event get published containing the current temperature and humidity. 
```bash
$ python iot.py 
```
See this [example](https://github.com/ibm-messaging/iot-visualization/) to visualize your events.