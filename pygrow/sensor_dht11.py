import dht
import machine

from variabili import *


def setup( pinNumber ):
    sensor = dht.DHT11(machine.Pin(pinNumber))
    return sensor


def measure(sensor):

    try:
        sensor.measure()
            
        temperature = sensor.temperature()
        humidity = sensor.humidity()
            
        return temperature,humidity
      
    except OSError as e:
        return "Errore di lettura dal sensore"
