from pycreate2 import Create2
import time

# Connect to global roomba through serial port, create object & set to safe mode
def Connect():
    global roomba

    # Serial port
    port = '/dev/ttyUSB0' #test comment
    print('Port set to \'/dev/ttyUSB0\'.')

    # global roomba object
    roomba = Create2(port)
    print('global roomba object created.')

    roomba.start()

    # Safe mode
    roomba.safe()
    print('global roomba set to safe mode.')

    

# Ensure global roomba 25% charged
def Ready():
    global roomba
    
    sensor = roomba.get_sensors()
    print("global roomba {sensor.battery_charge} / {sensor.battery_capacity} charged")

def Dance():
    global roomba
    # Backward
    roomba.drive_direct(-190, -190)
    time.sleep(2)

    for x in range(4):
        global roomba
        # Right
        roomba.drive_direct(190, 0)
        time.sleep(2)
        # Left
        # global roomba.drive_direct(0, 200)
        # time.sleep(1)
        
        # Forward
        roomba.drive_direct(190, 190)
        time.sleep(2)
        
    # Forward
    roomba.drive_direct(190, 190)
    time.sleep(2)

    # Right
    # global roomba.drive_direct(200, 0)
    # Stop
    roomba.drive_stop()

def Dock():
    global roomba
    roomba.close()