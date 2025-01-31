
from variabili import *

import wifi
import pygrow

# connessione al wifi...
#if not wifi.connettiWifi():
if not wifi.creaReteWifi():
    print("NON CONNESSO!!!")
    exit(1)

print("Connettiti a PyGrow3")
print("Pass: 12345678")
print("Apri http://192.168.4.1/")
pippo = pygrow.PyGrow()
pippo.run()

