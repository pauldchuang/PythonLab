import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            message = input("Enter message for server: ")
            await websocket.send(message)
            print("Message sent to server")

            response = await websocket.recv()
            print(f"Received response from server: {response}")

asyncio.run(send_message())
