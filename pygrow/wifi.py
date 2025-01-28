from variabili import *

import network
import time


def connettiWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # connette l'interfaccia WLAN alla rete Wifi SSID con chiave KEY
    wlan.connect(SCHOOL_SSID, SCHOOL_KEY)

    # configurazione di rete: Questi numeri potrebbero funzionare a scuola, con una opportuna x fra 1 e 254
    wlan.ifconfig( (IP_ESP32,MASK_ESP32,GW_ESP32,DNS_ESP32) )

    for n in range(6):
        if wlan.isconnected():
            break
        print("Connecting...")
        time.sleep(0.5)
    else:
        print("NOT CONNECTED!!!")
        return False

    print("CONNECTED")
    return True


def creaReteWifi():
    # crea l'oggetto interfaccia WLAN con opzione network.AP_IF
    wlan = network.WLAN(network.AP_IF)

    # Imposta il nome (si chiama SSID) della rete Wifi
    wlan.config(ssid=LOCAL_SSID , security=3 , key=LOCAL_KEY)

    # attivala
    wlan.active(True)
    time.sleep(0.5)
    
    print(f"Created Wifi Network {LOCAL_SSID}...")
    return True


if __name__ == "__main__":
    print("PROVA DI CONNESSIONE...")
    connettiWifi()
    
    