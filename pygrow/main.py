

from variabili import *

import wifi
import pygrow

# connessione al wifi...
if not wifi.connettiWifi():
    print("NON CONNESSO!!!")
    exit(1)

pippo = pygrow.PyGrow()
pippo.run()

