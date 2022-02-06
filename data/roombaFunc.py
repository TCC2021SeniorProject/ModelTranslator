from pycreate2 import Create2
import time

# Connect to roomba through serial port, create object & set to safe mode
def Connect():
    # Serial port
    port = '/dev/ttyUSB0'
    print('Port set to \'/dev/ttyUSB0\'.')

    # Roomba object
    roomba = Create2(port)
    print('Roomba object created.')

    roomba.start()

    # Safe mode
    roomba.safe()
    print('Roomba set to safe mode.')

    return roomba

# Ensure roomba 25% charged
def Ready(roomba):
    sensor = roomba.get_sensors()
    if sensor.BatteryCharge() > sensor.BatteryCapacity()/4:
        return True

    return False

print("Test!")
print("Test!")

def Dance(roomba):

    # Backward
    roomba.drive_direct(-200, -200)
    time.sleep(2)

    for x in range(4):
        # Left
        roomba.drive_direct(0, 200)
        time.sleep(1)

        # Forward
        roomba.drive_direct(200, 200)
        time.sleep(1)

    # Right
    # roomba.drive_direct(200, 0)
    # Stop
    roomba.drive_stop()

def Dock(roomba):
    roomba.seekdock()
    roomba.close()

# Test
roomba = Connect()
if Ready(roomba):
    Dance(roomba)
    Dock(roomba)
else:
    print("Roomba < 25 charged")
