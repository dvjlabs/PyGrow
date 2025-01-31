import machine
import time
from bme280 import BME280

def setup(scl_pin, sda_pin):
    
    i2c = machine.I2C(scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin))
    bme = BME280(i2c=i2c)
    
    return bme
    
def measure(bme):
    
    # Scansione
    temperature = bme.temperature
    pressure = bme.pressure
#    humidity = bme.humidity
    
    return temperature, pressure


if __name__ == "__main__":
    
    print("Prova sensore")
    sensor = sensorSetup(i2c_scl_pin, i2c_sda_pin)
    for i in range(6):
        temp, press = measure(sensor)
        print("Misurazioni", temp, press)
        
        time.sleep(0.5)

    