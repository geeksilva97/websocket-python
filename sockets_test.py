
#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

import serial

async def time(websocket, path):
    while True:
        data = await websocket.recv()
        print(data)
        ser = serial.Serial('/dev/ttyUSB0', 2400, timeout=1, parity=serial.PARITY_NONE)

        # jogando pó mágico
        values = bytearray([5,13])
        ser.write(values)
        
        peso = ser.readline()
        peso = peso[1:len(peso)-1]
        print('peso lido', peso)        
        ser.close()
        await websocket.send(peso.decode())
        print('enviado: hello world')
        #now = datetime.datetime.utcnow().isoformat() + "Z"
        #await websocket.send(now)
        #await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
