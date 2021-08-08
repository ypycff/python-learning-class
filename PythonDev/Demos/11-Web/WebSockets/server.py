import asyncio
import websockets

async def onconnect(websocket, uri):

    while True:
        datain = await websocket.recv()
        print("From client: %s" % datain)

        dataout = "ECHO! " + datain        
        print("To client:   %s" % dataout)

        await websocket.send(dataout)

start_server = websockets.serve(onconnect, 'localhost', 8002)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()