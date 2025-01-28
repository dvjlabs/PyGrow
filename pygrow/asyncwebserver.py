
# Import necessary modules
import asyncio
import socket
import time
import random
   
# Asynchronous functio to handle client's requests
async def handle_client(reader, writer):
    global state
    
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
    valoreTemperatura = 34#moduloDHT11.controllaTemperatura
    html = html.replace('BME280TEMP', str(valoreTemperatura))
    # SUOLO1
    html = html.replace('SUOLO1', str(random.randint(-10,40)))
    # SUOLO2
    html = html.replace('SUOLO2', str(random.randint(-10,40)))
    # TEMP1
    html = html.replace('TEMP1', str(random.randint(-10,40)))
    # TEMP2
    html = html.replace('TEMP2', str(random.randint(-10,40)))
    # BME280PRESS
    html = html.replace('BME280PRESS', str(random.randint(-10,40)))
    # DHT11TEMP
    html = html.replace('DHT11TEMP', str(random.randint(-10,40)))
    # DHT11PRESS
    html = html.replace('DHT11PRESS', str(random.randint(-10,40)))
    
    # Send the HTTP response and close the connection
    writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(html)
    await writer.drain()
    await writer.wait_closed()
    print('Client Disconnected')
    

async def main():
    # Start the server and run the event loop
    print('Setting up server')
    server = asyncio.start_server(handle_client, "0.0.0.0", 80)
    asyncio.create_task(server)
    
    while True:
        # Add other tasks that you might need to do in the loop
        await asyncio.sleep(60)
        print('This message will be printed every 5 seconds')
        

def run():
    # Create an Event Loop
    loop = asyncio.get_event_loop()
    # Create a task to run the main function
    loop.create_task(main())

    try:
        # Run the event loop indefinitely
        loop.run_forever()
    except Exception as e:
        print('Error occured: ', e)
    except KeyboardInterrupt:
        print('Program Interrupted by the user')
        

if __name__ == '__main__':
    run()
