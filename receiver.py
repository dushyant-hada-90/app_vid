import asyncio, websockets, json

async def handler(ws):
    print("📡 Client connected")
    async for message in ws:
        try:
            data = json.loads(message)
            print(f"👉 Index Finger Coordinates: {data}")
        except json.JSONDecodeError:
            print("⚠️ Received non-JSON data")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("🟢 WebSocket Server listening on port 8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
