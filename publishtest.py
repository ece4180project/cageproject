#Program to read the values of Temp and Hum from the DHT11 sensor and send it over to AWS-IOT

#Website: www.circuitdigest.com

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient #Import from AWS-IoT Library
import time#To create delay
from datetime import date, datetime #To get date and time



myMQTTClient = AWSIoTMQTTClient("RaspPi")
myMQTTClient.configureEndpoint("a1ww2s1rydoghz-ats.iot.us-east-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/pi/Desktop/deviceSDK/certs/AmazonRootCA1.pem", "/home/pi/Desktop/deviceSDK/certs/ad9dafb999-private.pem.key", "/home/pi/Desktop/deviceSDK/certs/ad9dafb999-certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

#sensor_name = button #we are using the DHT11 sensor
#sensor_pin = 17 #The sensor is connected to GPIO17 on Pi



time.sleep(2) #wait for 2 secs

connecting_time = time.time() + 10

if time.time() < connecting_time:  #try connecting to AWS for 10 seconds
    myMQTTClient.connect()
    myMQTTClient.publish("DHT11/info", "connected", 0)
    print("MQTT Client connection success!")
else:
    print("Error: Check your AWS details in the program")

    
time.sleep(2) #wait for 2 secs
value = 1;

while 1: #Infinite Loop
    i=1;
    fp=open("water bottle.txt","r")
    fp2=open("wheel.txt","r")
    fp3=open("temperature.txt","r")
    watervalues=fp.readlines()
    wheelvalues=fp2.readlines()
    tempvalues=fp3.readlines()
    now = datetime.utcnow() #get date and time 
    current_time = now.strftime('%Y-%m-%dT%H:%M:%SZ') #get current time in string format 
    
 #   value = button.read_retry(sensor_name, sensor_pin) #read from sensor and save respective values in temperature and humidity varibale  
    time.sleep(2) #Wait for 2 sec then update the values

    #prepare the payload in string format 
    #payload = '{ "timestamp": "' + current_time + '","temperature": '  + str(value) + ' }'
    payload=",".join(wheelvalues)
    payload2=",".join(watervalues)
    payload3=",".join(tempvalues)
    if (payload2.find("w")!=-1):
        myMQTTClient.publish("DHT11/data2", "Water Bottle Empty \n" + payload2, 0) #publish the payload
        print(payload2) #print payload for reference
        time.sleep(1) #Wait for 2 sec then update the values
    print(payload) #print payload for reference 
    myMQTTClient.publish("DHT11/data", payload, 0) #publish the payload
    myMQTTClient.publish("DHT11/data3", payload3, 0) #publish the payload
    value = value+1

    time.sleep(20) #Wait for 2 sec then update the values
