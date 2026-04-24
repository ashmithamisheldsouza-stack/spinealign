import asyncio
from bleak import BleakScanner, BleakClient

UART_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
TARGET_ADDRESS = "DF:BA:A2:8E:9D:8A"

def handle_data(sender, data):
    print("Received:", data.decode())

async def main():
    print("Scanning...")
    devices = await BleakScanner.discover()

    target = None

    for d in devices:
        print("Found:", d.name, d.address)
        if d.address == TARGET_ADDRESS:
            target = d

    if target is None:
        print("❌ Device not found")
        return

    print("Connecting to:", target.address)

    async with BleakClient(target.address) as client:
        print("✅ Connected!")
        await client.start_notify(UART_UUID, handle_data)
        await asyncio.sleep(60)

asyncio.run(main())