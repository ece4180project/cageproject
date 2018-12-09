import time
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
file=open("temperature.txt",'w')
file.close()
happy=time.time()
try:
    while(1):
            file3=open("temperature.txt",'a')
            x=time.time()-happy
            if(x>1):
                happy=time.time()
                humidity,temperature = Adafruit_DHT.read_retry(11,4)
                print('here')
                file3.write("time: " + str(x) + "seconds, " )
                file3.write("temperature: " + str(temperature)+"C, Humidity " + str(humidity) + "% \n")
            file3.close()
except KeyboardInterrupt:
    pass   # Go to next line
GPIO.cleanup()              # Make all GPIO pins LOW    
