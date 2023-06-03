#Importieren der benötigten Module:
from time import sleep
from umqtt.simple import MQTTClient # ist bei esp8266 micropython eingebaut
from BME280_1 import BME280
import batterie
from machine import I2C,Pin,RTC,DEEPSLEEP,deepsleep,reset_cause,DEEPSLEEP_RESET

#Diese Funktion wird beim Empfang aufgerufen ( subscribe Topic)
def sub_cb(topic, msg):
    topic=topic.decode()
    msg= msg.decode()
    print(f'empfangen: {topic} = {msg}')

class Mqtt():
''' die SERVER -IP  aus Router ablesen, am besten feste IP einstellen
    USER und PASSWORD = user und pw zum raspi
'''
    def __init__(self):
        # Zugangsdaten des Raspberry Pi im Netz
        SERVER    = '192.168.178.xx'
        CLIENT_ID = 'ESP8266'
        PORT      = 1883
        USER      = 'pi'
        PASSWORD  = 'pi'
        self.client = MQTTClient(CLIENT_ID, SERVER, port=PORT ,user=USER, password=PASSWORD)
        self.client.set_callback(sub_cb)
        self.connected=False
        
    #Diese Funktion wird beim Senden aufgerufen ( publish Topic)
    def publish(self,topic,x):
        print(f'gesendet: {topic} ={x}')
        msg   = f'{x}'.encode()
        topic = topic.encode()
        self.client.publish(topic, msg)  # Publish sensor data to MQTT topic
        

    def connect(self):
        try:
            self.client.connect()
            self.connected=True
        except:
            self.connected=False
            
    def disconnect(self):
        self.client.disconnect()
        
def schlaf(*,seconds=10):
    t= int(seconds*1000)
    rtc = RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, t)
    deepsleep()


########  Hauptprogramm ################
#start hier...
def run():
    # construct an I2C bus für den Sensor BME
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
    bme = BME280(address=0x76, i2c=i2c)
    mqtt=Mqtt()
    mqtt.connect()
    if mqtt.connected:
        try:
            mqtt.publish('temp',round(bme.temperature,1))
            sleep(.1)
            mqtt.publish('humi',round(bme.humidity,1))
            sleep(.1)
            mqtt.publish('press',round(bme.pressure,1))
            sleep(.2)
            mqtt.publish('volt',volt.batterie.volt())
            sleep(.2)
        except Exception as e:
            print(e)
        mqtt.disconnect()

run()
schlaf(seconds=60*60)
