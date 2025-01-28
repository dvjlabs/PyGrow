# THE web server
import socket
import time

import random

import sensoredht11
import moisture
import sensords18


def run(sens_dht11,sens_hum1,sens_hum2,sens_ds18):
    # ....
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 80))
    server.listen(5) # max number of simultaneous connections
    #server.setblocking(False)

    file = open('base.html', "r")
    content = file.read()
    file.close()

    while True:
        
        conn,addr = server.accept()
        print('Got a connection from ', str(addr))
        
        conn.settimeout(3.0)
        request = conn.recv(1024)
        conn.settimeout(None)
        
       
        # SOSTITUZIONI!!!
        html = content
        
        # BME280TEMP
        valoreTemperatura = 12
        html = html.replace('BME280TEMP', str(valoreTemperatura))
        # SUOLO1
        s1 = moisture.misura(sens_hum1)
        html = html.replace('SUOLO1', str(s1))
        # SUOLO2
        s2 = moisture.misura(sens_hum2)
        html = html.replace('SUOLO2', str(s2))
        
        # TEMP1
        temp1,temp2 = sensords18.scan(sens_ds18)
        html = html.replace('TEMP1', str(temp1))
        html = html.replace('TEMP2', str(temp2))
        # BME280PRESS
        html = html.replace('BME280PRESS', str(random.randint(-10,40)))
        
        temp_dht11, press_dht11 = sensoredht11.misura(sens_dht11)
        # DHT11TEMP
        html = html.replace('DHT11TEMP', str(temp_dht11))
        # DHT11PRESS
        html = html.replace('DHT11PRESS', str(press_dht11))
        
        # ---------------------------------------
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(html)
        conn.close()
    
    return

