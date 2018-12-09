import pigpio
import time
import RPi.GPIO as GPIO
servo_pin = 21      # Initializing the GPIO 21 for servo motor
GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(servo_pin, GPIO.OUT)     # Declaring GPIO 21 as output pin
p = GPIO.PWM(servo_pin, 50)     # Created PWM channel at 50Hz frequency
p.start(2.5)                    
pi=pigpio.pi()
pi.set_mode(19, pigpio.INPUT)
pi.set_pull_up_down(19,pigpio.PUD_DOWN)
pi.set_mode(6, pigpio.INPUT)
pi.set_pull_up_down(6,pigpio.PUD_DOWN)
pi.set_mode(17, pigpio.OUTPUT)
pi.set_mode(27, pigpio.OUTPUT)
file=open("water bottle.txt",'w')
file.close()
file=open("wheel.txt",'w')
file.close()
file=open("temperature.txt",'w')
file.close()
int=0;
wheel_value=1;
water_bottle=0;
initial=0;
p.ChangeDutyCycle(2.5)  # Move servo to 0 degrees
#sensor_args={ '11': Adafruit_DHT.DHT11,
        #      '22': Adafruit_DHT.DHT22,
       #       '2302': Adafruit_DHT.AM2302 }
#if len(sys.argv) == 3 and sys.argv[1] in sensor_ars:
  #  sensor=sensor_args[sys.argv[1]]
  #  pin = sys.argv[2]
#else:
   # print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
  #  print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
  #  sys.exit(1)
try:
    while(1):

        if(int%7000==0):
            p.ChangeDutyCycle(2.5)  # Move servo to 90 degrees
          
        elif(int%1000==0 ):
            p.ChangeDutyCycle(12.5)  # Move servo to 90 degrees
        file=open("water bottle.txt",'a')
        file2=open("wheel.txt",'a')
        pin19=pi.read(19)
        pin6=pi.read(6)
        if(pin19!=water_bottle):
            water_bottle=pin19
            file.write("water bottle:"+str(pin19)+" time:" + str(int*.001)+"\n")
        if(pin6!=wheel_value):
            wheel_value=pin6
            if (initial==0):
                initial=1
                file2.write("wheel 1 spin time:" + str(int*.001)+"\n")
            else:
                initial=0
        if (pin19):
            pi.write(17,1)
        else:
            pi.write(17,0)
        if(pin6):
            pi.write(27,0)
        else:
            pi.write(27,1)
        file.close()
        file2.close()
        time.sleep(.001)
        int=int+1;
except KeyboardInterrupt:
    pass   # Go to next line
GPIO.cleanup()              # Make all GPIO pins LOW    
