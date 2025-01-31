import time
from machine import I2C, Pin
from I2C_LCD import I2cLcd


def setupDisplay(pin1,pin2):
    i2c = I2C(scl=Pin(pin1), sda=Pin(pin2), freq=400000)
    devices = i2c.scan()
    for device in devices:
        lcd = I2cLcd(i2c, device, 2, 16)
        return lcd

def mostraDisplay(lcd,umidità1,umidità2,tempH2O_1,tempH2O_2,Air_temp1,Air_press,Air_temp2,Air_humid):
    lcd.clear()
    dizionario = {"Soil moisture 1": f"{umidità1} %",
                  "Soil moisture 2": f"{umidità2} %",
                  "Water temp1": f"{tempH2O_1}°C",
                  "Water temp2": f"{tempH2O_2}°C",
                  "Air temp1 BME280": f"{Air_temp1}°C",
                  "Air press BME280": f"{Air_press} hPA",
                  "Air temp2 DHT11": f"{Air_temp2} hPA",
                  "Air humid DHT11": f"{Air_humid} %"}
    for n in range(2):
        for key in dizionario:
            lcd.move_to(0,0)
            lcd.putstr(key)
            lcd.move_to(0,1)
            lcd.putstr(dizionario[key])
            
            time.sleep(3)
            lcd.clear()
            time.sleep(0.6)
            
    lcd.move_to(0,0)
    lcd.putstr("Loading new")
    lcd.move_to(0,1)
    lcd.putstr("values...")
    return


