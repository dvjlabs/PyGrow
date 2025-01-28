
# sensors
import moisture
import sensor_dht11
import sensor_ds18

# Import necessary modules
import asyncio
import socket
import time

import random

# class
class PyGrow:
    
    def __init__(self):
        self.sens_dht11 = 0#sensor_dht11.setup(pinDHT11)
        self.sens_hum1 = 0#moisture.setup(pinMoisture1)
        self.sens_hum2 = 0#moisture.setup(pinMoisture2)
        self.sens_ds18 = 0#sensor_ds18.setup(pinDS18)
    
        self.dht11_value = (0,0)
        self.hum1_value = 0
        self.hum2_value = 0
        self.ds18_value = (0,0)
        self.bme280_value = (0,0)

    async def main(self):
        # Start the server and run the event loop
        print('Setting up server')
        server = asyncio.start_server(self.handle_client, "0.0.0.0", 80)
        asyncio.create_task(server)
        
        while True:
            # Add other tasks that you might need to do in the loop
            await asyncio.sleep(60)
            print('60 seconds passed: sensors measuring...')
            self.measure()


    def run(self):
        # Create an Event Loop
        loop = asyncio.get_event_loop()
        # Create a task to run the main function
        loop.create_task(self.main())

        try:
            # Run the event loop indefinitely
            loop.run_forever()
        except Exception as e:
            print('Error occured: ', e)
        except KeyboardInterrupt:
            print('Program Interrupted by the user')
    

    # Asynchronous functio to handle client's requests
    async def handle_client(self, reader, writer):
        print("Client connected")
        request_line = await reader.readline()
        print('Request:', request_line)
        
        # Skip HTTP request headers
        while await reader.readline() != b"\r\n":
            pass
        
        request = str(request_line, 'utf-8').split()[1]
        print('Request:', request)

        # SOSTITUZIONI!!!
        file = open("base.html")
        content = file.read()
        file.close()
        html = content
        
        # BME280TEMP
        html = html.replace('BME280TEMP', str(self.bme280_value[0]))
        # BME280PRESS
        html = html.replace('BME280PRESS', str(self.bme280_value[1]))
        # SUOLO1
        html = html.replace('SUOLO1', str(self.hum1_value))
        # SUOLO2
        html = html.replace('SUOLO2', str(self.hum2_value))
        # TEMP1
        html = html.replace('TEMP1', str(self.ds18_value[0]))
        # TEMP2
        html = html.replace('TEMP2', str(self.ds18_value[1]))
        # DHT11TEMP
        html = html.replace('DHT11TEMP', str(self.dht11_value[0]))
        # DHT11HUM
        html = html.replace('DHT11HUM', str(self.dht11_value[1]))
        
        # Send the HTTP response and close the connection
        writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        writer.write(html)
        await writer.drain()
        await writer.wait_closed()
        print('Client Disconnected')
        return

    
    def measure(self):
        self.dht11_value = random.randint(1,30),random.randint(1,30)
        #self.dht11_value = self.sens_dht11.measure()
        
        self.hum1_value = random.randint(1,30)
        #self.hum1_value = self.sens_hum1.measure()
        
        self.hum2_value = random.randint(1,30)
        #self.hum2_value = self.sens_hum2.measure()
        
        self.ds18_value = random.randint(1,30),random.randint(1,30)
        #self.ds18_value = self.sens_ds18.measure()
        
        self.bme280_value = random.randint(1,30),random.randint(1,30)
        #self.bme280_value = self.sens_bme280.measure()
        return
