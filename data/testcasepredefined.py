# Written by Cael Shoop.

import time
from pycreate2 import Create2

def com_dance():
    roomba.drive_direct(-190, -190)
    time.sleep(1)
    roomba.drive_direct(-400, 400)
    time.sleep(1)
    roomba.drive_direct(190, 190)
    time.sleep(1)
    roomba.drive_direct(-400, 400)
    time.sleep(1)
    roomba.drive_direct(190, 190)
    time.sleep(1)
    roomba.drive_direct(-400, 400)
    time.sleep(1)
    roomba.drive_direct(190, 190)
    time.sleep(1)
    roomba.drive_direct(-400, 400)
    time.sleep(1)
    roomba.drive_direct(190, 190)
    time.sleep(1)
    roomba.drive_stop()
    done = 1


def com_dock():
    roomba.seek_dock()
    time.sleep(2)
    roomba.close()


def com_init():
    global done
    done = 0
    try:
        roomba = Create2('/dev/ttyUSB0')
    except:
        roomba = Create2('/dev/ttyUSB1')


def Initialized():
    roomba.start()
    roomba.full()