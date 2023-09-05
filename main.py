import asyncio
from bleak import BleakScanner, BLEDevice

TARGET_DEVICE = "BlueToothAddress"
SAVE_TO_FILENAME = "Filename"

def callback(sender: BLEDevice, advertisement_data):
    if sender.address == TARGET_DEVICE:
        data_bytes = advertisement_data.manufacturer_data[343]
        
        heart_rate = data_bytes[3]
        print(f"Heart rate: {heart_rate} BPM")
        with open(SAVE_TO_FILENAME,'w') as f:
            f.write(str(heart_rate))

async def scan_for_devices():
    scanner = BleakScanner(detection_callback=callback)
    await scanner.start()
    try:
        while True:
            await asyncio.sleep(1.0)  
    except KeyboardInterrupt:
        pass
    finally:
        await scanner.stop()
        print("Scanner stopped.")


loop = asyncio.get_event_loop()
loop.run_until_complete(scan_for_devices())
