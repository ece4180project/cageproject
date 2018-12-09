# ECE 4180 Embedded Design Project : Cloud-connected Pet Cage by Zechen Lu, Phillip Yamin, and Chris Chen
A final project for ECE 4180 consisting of an IoT pet cage that connects to Amazon Web Services (AWS) with the following features:
* Automated Food Dispensing
* Water Level Detection (with emailled refill reminders via AWS)
* Temperature and Humidity Detection with DHT11 Sensor
* Hamster Wheel Exercise Monitor 

The main idea behind this project was to provide a proof-of-concept of a "hands-off" pet cage, that allows a busy person a degree of automation when it comes to caring for their caged pet. 

Demonstration Video of Cage Features:
[![AAAAA](http://img.youtube.com/vi/2MsN8gpT6jY/0.jpg)](http://www.youtube.com/watch?v=2MsN8gpT6jY "Github Pages")

## Design

The project was programmed entirely with the Amazon AWS Python SDK to provide cloud-connected services for the cage, with a Raspberry Pi 3 acting as the host computing element that ran the code.

### Food Dispensing

Food dispensing was done by mounting an HS-422 Servo that used a wire-connected assembly to manipulate the lever-arm of the dispensing unit, which was fed from a storage hopper fashioned out of a milk jug. A periodic timer in the code is set to actuate the Servo via PWM at set intervals. For demonstration purposes, this was set to very short intervals (30 seconds), but it is readily adjustable.

### Water Level Detection w/ Email Reminders

Water level detection was accomplished by installing a float switch in the water bottle, which switches a digital OFF signal to the Pi when the water level gets too low. This causes a packet to be sent via MQTT to Amazon servers detailling the time the water level fell while also sending a reminder email.

### Temperature Sensor

Using a pre-built library, we used a DHT 11 Sensor hooked up directly to the Pi to take temperature readings.

### Hamster Wheel Exercise Monitor

Exercise detection was done with a hall-effect sensor mounted to the cage wall in proximity to a spinning hamster wheel, which had a magnet attached to the outer rim. The wheel would trigger the sensor once every spin, allowing us to track physical activity.
