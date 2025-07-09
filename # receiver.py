# # receiver.py
# import asyncio
# import websockets

# async def handler(websocket):
#     async for message in websocket:
#         print(f"Index Finger: {message}")

# async def main():
#     async with websockets.serve(handler, "0.0.0.0", 8765):
#         print("Listening on ws://0.0.0.0:8765")
#         await asyncio.Future()  # run forever

# asyncio.run(main())


# receiver.py
import asyncio
import websockets

async def handler(websocket):
    print("Client connected")
    async for message in websocket:
        print(f"Received: {message}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("WebSocket Server Running on port 8765")
        await asyncio.Future()

asyncio.run(main())
