from machine import ADC, Pin
from time import sleep
from variabili import *

def setup(pin):
    moisture_sensor = ADC(pin) 
    moisture_sensor.atten(ADC.ATTN_11DB) 
    moisture_sensor.width(ADC.WIDTH_12BIT) 
    return moisture_sensor
    
def measure( sensor ):
    raw_value = sensor.read() 
    percentage = int((raw_value / 2030) * 100)
    return percentage 

if __name__ == "__main__":
    print("PROVA MISURA UMIDITA")
    sensore = setupSensore(PIN_UMIDITA1)
    misura(sensore)
    sensore = setupSensore(PIN_UMIDITA2)
    misura(sensore)
