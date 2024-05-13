import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Received message from client: {message}")
        response = f"Server received: {message}"
        await websocket.send(response)
        print(f"Sent response to client: {response}")

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
