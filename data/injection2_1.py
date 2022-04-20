import time
import piInterface as piI
import PyLidar3


def Com_initialized():
    piI.Connect()
    pi0, pi1 = piI.ShellBoth('python3 -i predefined2.py\n')
    print(str(pi0) + '\n' + str(pi1))
    while 'connected' not in pi0:
        time.sleep(.1)
        pi0 = piI.Shell('', 0)
        print(pi0)
    while 'connected' not in pi1:
        time.sleep(.1)
        pi1 = piI.Shell('', 1)
        print(pi1)


def Scanning():
    out = piI.Shell('scan\n', self.piNum)
    print(out)
    await asyncio.sleep(0.01)
    while 'scanned' not in out:
        time.sleep(.1)
        out = piI.Shell('', self.piNum)
        print(out)


def Undock():
    out = piI.Shell('undock\n', self.piNum)
    print(out)
    await asyncio.sleep(0.01)
    while 'undocked' not in out:
        time.sleep(.1)
        out = piI.Shell('', self.piNum)
        print(out)


def Turning():
    if self.piNum == 0:
        out = piI.Shell('rotate ' + str(rp0Angle), self.piNum)
    else:
        out = piI.Shell('rotate ' + str(rp1Angle), self.piNum)
    print(out)
    await asyncio.sleep(0.01)
    while 'rotated' not in out:
        time.sleep(.1)
        out = piI.Shell('', self.piNum)
        print(out)


def Moving():
    if self.piNum == 0:
        out = piI.Shell('move ' + str(rp0Distance), self.piNum)
    else:
        out = piI.Shell('move ' + str(rp1Distance), self.piNum)
    print(out)
    await asyncio.sleep(0.01)
    while 'moved' not in out:
        time.sleep(.1)
        out = piI.Shell('', self.piNum)
        print(out)


def Docking():
    out = piI.Shell('dock', self.piNum)
    print(out)
    await asyncio.sleep(0.01)
    while 'docked' not in out:
        time.sleep(.1)
        out = piI.Shell('', self.piNum)
        print(out)


def Com_finished():
    pi0, pi1 = piI.ShellBoth('disconnect')
    while 'disconnected' not in pi0:
        time.sleep(.1)
        pi0 = piI.Shell('', 0)
    while 'disconnected' not in pi1:
        time.sleep(.1)
        pi1 = piI.Shell('', 1)
    piI.Disconnect()
    time.sleep(3)