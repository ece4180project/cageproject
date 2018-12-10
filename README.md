# ECE 4180 Embedded Design Project : Cloud-connected Pet Cage by Zechen Lu, Phillip Yamin, and Chris Chen
A final project for ECE 4180 consisting of an IoT pet cage that connects to Amazon Web Services (AWS) with the following features:
* Automated Food Dispensing
* Water Level Detection (with emailled refill reminders via AWS)
* Temperature and Humidity Detection with DHT11 Sensor
* Hamster Wheel Exercise Monitor 

The main idea behind this project was to provide a proof-of-concept of a "hands-off" pet cage, that allows a busy person a degree of automation when it comes to caring for their caged pet. 

Demonstration Video of Cage Features:


[![Demo Video](http://img.youtube.com/vi/PQlBYB-Skgk/0.jpg)](http://www.youtube.com/watch?v=PQlBYB-Skgk "Demonstration Video")

## Design

The project was programmed entirely with the Amazon AWS Python SDK to provide cloud-connected services for the cage, with a Raspberry Pi 3 acting as the host computing element that ran the code.

To recreate the project, you will need the following things:

* Raspberry Pi 3B with Raspbian Installed and Cobbler Breadboard Adapter 

*[Full Repository of Python Code Available here (must be run on seperate IDEs/Runners)](https://github.com/ece4180project/cageproject)

* A typical pet cage suited for gerbils/rabbits/etc.

* Legos or similar provision for constructing a frame for the feeder.

* Breadboard and patch cables

* DHT11 Sensor with Python Library  [Connection Instructions and Python Code available here](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/)

* HS-422 Servo

* A water bottle that can be drilled near the bottom

* A right-angle float switch, such as [this](https://www.banggood.com/Side-mounted-Liquid-Water-Level-Sensor-Right-Angle-Float-Switch-p-945298.html?cur_warehouse=CN)

* A typical hamster wheel

* A Sunfounders Hall Effect Switch [Avaialble here](https://www.amazon.com/SunFounder-Switch-Sensor-Arduino-Raspberry/dp/B013G5N03O)

* Magnets for Hall Effect

* An improvised storage hopper for the food dispensing system.

* 5V Power Supply with breadboard friendly output terminals

### Connecting Pi to Amazon Web Services and sending data



### Food Dispensing

Food dispensing was done by mounting an HS-422 Servo that used a wire-connected assembly to manipulate the lever-arm of the dispensing unit, which was fed from a storage hopper fashioned out of a milk jug. A periodic timer in the code is set to actuate the Servo via PWM at set intervals. For demonstration purposes, this was set to very short intervals (30 seconds), but it is readily adjustable in the code.

  The Servo is connected to the power supply's +5V and GND (with the power supply GND tied to the Raspberry Pi GND) with the Servo Control Pin connected to the Pi's GPIO Pin 21. The Servo position is adjusted by setting the appropriate duty cycle for each position.

### Water Level Detection w/ Email Reminders

Water level detection was accomplished by installing a float switch in the water bottle, which switches a digital OFF signal to the Pi when the water level gets too low. The code will then read this signal off of Pi GPIO Pin 19 connected to the float switch, set up as an Input with an internal pulldown enabled. This causes a packet to be sent via MQTT to Amazon servers detailling the time the water level fell while also sending a reminder email.

The internal pulldown resistor allows for the direct connection of the two float switch leads to GND and the GPIO Pin with no external resistors.

### Temperature Sensor

Using a pre-built Python library available [here](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/), we used a DHT 11 Sensor hooked up directly to the Pi to take temperature readings.

The DHT 11 was connected as shown below:
![DHT11](http://www.circuitbasics.com/wp-content/uploads/2015/12/How-to-Setup-the-DHT11-on-the-Raspberry-Pi-Three-pin-DHT11-Wiring-Diagram.png "DHT11")

### Hamster Wheel Exercise Monitor

Exercise detection was done with a hall-effect sensor mounted to the cage wall in proximity to a spinning hamster wheel, which had a magnet attached to the outer rim. The wheel would trigger the sensor once every spin, allowing us to track physical activity. The Hall Effect Sensor is connected to GPIO Pin 6 with an internal pulldown enabled, with the two leads connected to the GPIO Pin and Ground directly.


