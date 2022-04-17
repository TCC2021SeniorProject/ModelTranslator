import asyncio
import time
import piInterface as piI
import PyLidar3

numLoops = 0
initialized = None #Channel variable
undock = None #Channel variable
dock = None #Channel variable
scan = None #Channel variable
turn = None #Channel variable
map = None #Channel variable
finished = None #Channel variable
move = None #Channel variable
disconnect = None #Channel variable
rp0On = False
rp1On = False
rp0State = 0
rp1State = 0
rp0Angle = 0.0
rp1Angle = 0.0
rp0Distance = 0.0
rp1Distance = 0.0
rp0ScanTime = 0.0
rp1ScanTime = 0.0
map1Rp0 = 0
map1Rp1 = 0
map2Rp0 = 0
map2Rp1 = 0

class CentralController:
	def __init__(self, ):
		global Pi0
		global Pi1
		pass

	async def Com_finished(self):
		pi0, pi1 = piI.ShellBoth('disconnect')
		while 'disconnected' not in pi0:
			time.sleep(.1)
			pi0 = piI.Shell('', 0)
		while 'disconnected' not in pi1:
			time.sleep(.1)
			pi1 = piI.Shell('', 1)
		piI.Disconnect()

		pass

	async def Com_disconnect(self):
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Finished(), Pi1.Finished(), )
		await self.Com_finished()
		global numLoops
		numLoops = numLoops +1
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Disconnecting(), Pi1.Disconnecting(), )
		await self.Com_undock()

	async def Com_dock(self):
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Docking(), Pi1.Docking(), )
		await self.Com_disconnect()

	async def Com_turn5(self):
		global rp0Angle
		rp0Angle = -90.0
		global rp1Angle
		rp1Angle = 90.0
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Turning(), Pi1.Turning(), )
		await self.Com_dock()

	async def Com_map2(self):
		global map2Rp0
		map2Rp0 = numLoops +1
		global map2Rp1
		map2Rp1 = numLoops +1
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Mapping(), Pi1.Mapping(), )
		await self.Com_turn5()

	async def Com_scan2(self):
		global rp0ScanTime
		rp0ScanTime = 2.0
		global rp1ScanTime
		rp1ScanTime = 2.0
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Scanning(), Pi1.Scanning(), )
		await self.Com_map2()

	async def Com_move4(self):
		global rp0Distance
		rp0Distance = 1.0
		global rp1Distance
		rp1Distance = 1.0
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Moving(), Pi1.Moving(), )
		await self.Com_scan2()

	async def Com_turn4(self):
		global rp0Angle
		rp0Angle = 90.0
		global rp1Angle
		rp1Angle = -90.0
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Turning(), Pi1.Turning(), )
		await self.Com_move4()

	async def Com_move3(self):
		global rp0Distance
		rp0Distance = 1.0
		global rp1Distance
		rp1Distance = 1.0
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Moving(), Pi1.Moving(), )
		await self.Com_turn4()

	async def Com_map1(self):
		global map1Rp0
		map1Rp0 = numLoops +1
		global map1Rp1
		map1Rp1 = numLoops +1
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Mapping(), Pi1.Mapping(), )
		await self.Com_move3()

	async def Com_scan1(self):
		global rp0ScanTime
		rp0ScanTime = 1.0
		global rp1ScanTime
		rp1ScanTime = 1.0
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Scanning(), Pi1.Scanning(), )
		await self.Com_map1()

	async def Com_turn3(self):
		global rp0Angle
		rp0Angle = 90.0
		global rp1Angle
		rp1Angle = -90.0
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Turning(), Pi1.Turning(), )
		await self.Com_scan1()

	async def Com_move2(self):
		global rp0Distance
		rp0Distance = 1.0
		global rp1Distance
		rp1Distance = 1.0
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Moving(), Pi1.Moving(), )
		await self.Com_turn3()

	async def Com_turn2(self):
		global rp0Angle
		rp0Angle = 90.0
		global rp1Angle
		rp1Angle = -90.0
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Turning(), Pi1.Turning(), )
		await self.Com_move2()

	async def Com_move1(self):
		global rp0Distance
		rp0Distance = 1.0
		global rp1Distance
		rp1Distance = 1.0
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Moving(), Pi1.Moving(), )
		await self.Com_turn2()

	async def Com_turn1(self):
		global rp0Angle
		rp0Angle = 180.0
		global rp1Angle
		rp1Angle = -180.0
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Turning(), Pi1.Turning(), )
		await self.Com_move1()

	async def Com_undock(self):
		global rp0Distance
		rp0Distance = -0.1
		global rp1Distance
		rp1Distance = -0.1
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Undock(), Pi1.Undock(), )
		await self.Com_turn1()

	async def Com_initialized(self):
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

		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Initalized(), Pi1.Initalized(), )
		await self.Com_undock()

class RaspberryPi0:
	def __init__(self, ):
		global CC
		global Pi1
		self.piNum = 0

	async def Empty1(self):
		pass

	async def Finished(self):
		await asyncio.sleep(0.01)
		await self.Empty1()

	async def Empty9(self):
		pass

	async def Mapping(self):
		await asyncio.sleep(0.01)
		await self.Empty9()

	async def Empty4(self):
		pass

	async def Undock(self):
		out = piI.Shell('undock\n', self.piNum)
		print(out)
		await asyncio.sleep(0.01)
		while 'undocked' not in out:
			time.sleep(.1)
			out = piI.Shell('', self.piNum)
			print(out)

		await asyncio.sleep(0.01)
		await self.Empty4()

	async def Empty5(self):
		pass

	async def Turning(self):
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

		await asyncio.sleep(0.01)
		await self.Empty5()

	async def Empty3(self):
		pass

	async def Moving(self):
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

		await asyncio.sleep(0.01)
		await self.Empty3()

	async def Empty8(self):
		pass

	async def Scanning(self):
		out = piI.Shell('scan\n', self.piNum)
		print(out)
		await asyncio.sleep(0.01)
		while 'scanned' not in out:
			time.sleep(.1)
			out = piI.Shell('', self.piNum)
			print(out)

		await asyncio.sleep(0.01)
		await self.Empty8()

	async def Empty7(self):
		pass

	async def Disconnecting(self):
		await asyncio.sleep(0.01)
		await self.Empty7()

	async def Empty6(self):
		pass

	async def Docking(self):
		out = piI.Shell('dock', self.piNum)
		print(out)
		await asyncio.sleep(0.01)
		while 'docked' not in out:
			time.sleep(.1)
			out = piI.Shell('', self.piNum)
			print(out)

		await asyncio.sleep(0.01)
		await self.Empty6()

	async def Empty2(self):
		pass

	async def Initalized(self):
		await asyncio.sleep(0.01)
		await self.Empty2()

class RaspberryPi1:
	def __init__(self, ):
		global CC
		global Pi0
		self.piNum = 1

	async def Empty1(self):
		pass

	async def Finished(self):
		await asyncio.sleep(0.01)
		await self.Empty1()

	async def Empty2(self):
		pass

	async def Initalized(self):
		await asyncio.sleep(0.01)
		await self.Empty2()

	async def Empty3(self):
		pass

	async def Moving(self):
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

		await asyncio.sleep(0.01)
		await self.Empty3()

	async def Empty4(self):
		pass

	async def Undock(self):
		out = piI.Shell('undock\n', self.piNum)
		print(out)
		await asyncio.sleep(0.01)
		while 'undocked' not in out:
			time.sleep(.1)
			out = piI.Shell('', self.piNum)
			print(out)

		await asyncio.sleep(0.01)
		await self.Empty4()

	async def Empty7(self):
		pass

	async def Disconnecting(self):
		await asyncio.sleep(0.01)
		await self.Empty7()

	async def Empty6(self):
		pass

	async def Docking(self):
		out = piI.Shell('dock', self.piNum)
		print(out)
		await asyncio.sleep(0.01)
		while 'docked' not in out:
			time.sleep(.1)
			out = piI.Shell('', self.piNum)
			print(out)

		await asyncio.sleep(0.01)
		await self.Empty6()

	async def Empty9(self):
		pass

	async def Mapping(self):
		await asyncio.sleep(0.01)
		await self.Empty9()

	async def Empty8(self):
		pass

	async def Scanning(self):
		out = piI.Shell('scan\n', self.piNum)
		print(out)
		await asyncio.sleep(0.01)
		while 'scanned' not in out:
			time.sleep(.1)
			out = piI.Shell('', self.piNum)
			print(out)

		await asyncio.sleep(0.01)
		await self.Empty8()

	async def Empty5(self):
		pass

	async def Turning(self):
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

		await asyncio.sleep(0.01)
		await self.Empty5()

loop = asyncio.get_event_loop()
Pi0 = RaspberryPi0()
Pi1 = RaspberryPi1()
CC = CentralController()
loop.run_until_complete(CC.Com_initialized())
loop.run_until_complete(Pi0.Initalized())
loop.run_until_complete(Pi1.Initalized())
