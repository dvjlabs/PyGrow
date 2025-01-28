import machine, onewire, ds18x20, time
from variabili import *


def setup(temperature_sensor_pin):
    ds_pin = machine.Pin(temperature_sensor_pin) # Pin sensore
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
    
    return ds_sensor


def measure( ds_sensor ):
    
    devices = ds_sensor.scan() # lista di dispositivi DS trovat
    print(len(devices))
    ds_sensor.convert_temp()
    time.sleep(0.5)
    listaTemp = []
    for device in devices:
        temperature = ds_sensor.read_temp(device)
        listaTemp.append(temperature)
    return listaTemp


if __name__ == "__main__":
    
    print("prova temperatura")
    sensor, device_prova = setup(ds18_pin1)
    for i in range(6):
        temp_prova = scan(sensor, device_prova)
        print("Misurazioni", temp_prova)
        
        time.sleep(0.5)
    