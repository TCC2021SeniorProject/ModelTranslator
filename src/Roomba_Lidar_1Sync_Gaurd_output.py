import asyncio
import time

initialized = None #Channel variable
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
		self.numLoops = 0

	async def Com_disconnect(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 15:
			self.numLoops = self.numLoops + 1
			await asyncio.sleep(0.01)
			await self.Com_undock()

	async def Com_dock(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 14:
			await asyncio.sleep(0.01)
			await self.Com_disconnect()

	async def Com_turn5(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 13:
			global rp0Angle
			rp0Angle = - 90.0
			global rp1Angle
			rp1Angle = 90.0
			await asyncio.sleep(0.01)
			await self.Com_dock()

	async def Com_map2(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 12:
			global map2Rp0
			map2Rp0 = self.numLoops + 1
			global map2Rp1
			map2Rp1 = self.numLoops + 1
			await asyncio.sleep(0.01)
			await self.Com_turn5()

	async def Com_scan2(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 11:
			global rp0ScanTime
			rp0ScanTime = 2.0
			global rp1ScanTime
			rp1ScanTime = 2.0
			await asyncio.sleep(0.01)
			await self.Com_map2()

	async def Com_move4(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 10:
			global rp0Distance
			rp0Distance = 1.0
			global rp1Distance
			rp1Distance = 1.0
			await asyncio.sleep(0.01)
			await self.Com_scan2()

	async def Com_turn4(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 9:
			global rp0Angle
			rp0Angle = 90.0
			global rp1Angle
			rp1Angle = - 90.0
			await asyncio.sleep(0.01)
			await self.Com_move4()

	async def Com_move3(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 8:
			global rp0Distance
			rp0Distance = 1.0
			global rp1Distance
			rp1Distance = 1.0
			await asyncio.sleep(0.01)
			await self.Com_turn4()

	async def Com_map1(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 7:
			global map1Rp0
			map1Rp0 = self.numLoops + 1
			global map1Rp1
			map1Rp1 = self.numLoops + 1
			await asyncio.sleep(0.01)
			await self.Com_move3()

	async def Com_scan1(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 6:
			global rp0ScanTime
			rp0ScanTime = 1.0
			global rp1ScanTime
			rp1ScanTime = 1.0
			await asyncio.sleep(0.01)
			await self.Com_map1()

	async def Com_turn3(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 5:
			global rp0Angle
			rp0Angle = 90.0
			global rp1Angle
			rp1Angle = - 90.0
			await asyncio.sleep(0.01)
			await self.Com_scan1()

	async def Com_move2(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 4:
			global rp0Distance
			rp0Distance = 1.0
			global rp1Distance
			rp1Distance = 1.0
			await asyncio.sleep(0.01)
			await self.Com_turn3()

	async def Com_turn2(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 3:
			global rp0Angle
			rp0Angle = 90.0
			global rp1Angle
			rp1Angle = - 90.0
			await asyncio.sleep(0.01)
			await self.Com_move2()

	async def Com_move1(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 2:
			global rp0Distance
			rp0Distance = 1.0
			global rp1Distance
			rp1Distance = 1.0
			await asyncio.sleep(0.01)
			await self.Com_turn2()

	async def Com_turn1(self):
		global rp0State
		global rp1State
		if rp0State and rp1State == 1:
			global rp0Angle
			rp0Angle = 180.0
			global rp1Angle
			rp1Angle = - 180.0
			await asyncio.sleep(0.01)
			await self.Com_move1()

	async def Com_undock(self):
		global rp0On
		global rp1On
		if rp0On and rp1On == True:
			global rp0Distance
			rp0Distance = - 0.1
			global rp1Distance
			rp1Distance = - 0.1
			await asyncio.sleep(0.01)
			await self.Com_turn1()

	async def Com_initialized(self):
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Initalized(), Pi1.Initalized(), )
		await self.Com_undock()

class RaspberryPi0:
	def __init__(self, ):
		global CC
		global Pi1
		self.piNum = 0

	async def Disconnecting(self):
		global rp0State
		rp0State = 0
		await asyncio.sleep(0.01)
		await self.Undock()

	async def Docking(self):
		global rp0State
		rp0State = 15
		await asyncio.sleep(0.01)
		await self.Disconnecting()

	async def Turning5(self):
		global rp0State
		rp0State = 14
		await asyncio.sleep(0.01)
		await self.Docking()

	async def Mapping2(self):
		global rp0State
		rp0State = 13
		await asyncio.sleep(0.01)
		await self.Turning5()

	async def Scanning2(self):
		global rp0State
		rp0State = 12
		await asyncio.sleep(0.01)
		await self.Mapping2()

	async def Moving4(self):
		global rp0State
		rp0State = 11
		await asyncio.sleep(0.01)
		await self.Scanning2()

	async def Turning4(self):
		global rp0State
		rp0State = 10
		await asyncio.sleep(0.01)
		await self.Moving4()

	async def Moving3(self):
		global rp0State
		rp0State = 9
		await asyncio.sleep(0.01)
		await self.Turning4()

	async def Mapping1(self):
		global rp0State
		rp0State = 8
		await asyncio.sleep(0.01)
		await self.Moving3()

	async def Scanning1(self):
		global rp0State
		rp0State = 7
		await asyncio.sleep(0.01)
		await self.Mapping1()

	async def Turning3(self):
		global rp0State
		rp0State = 6
		await asyncio.sleep(0.01)
		await self.Scanning1()

	async def Moving2(self):
		global rp0State
		rp0State = 5
		await asyncio.sleep(0.01)
		await self.Turning3()

	async def Turning2(self):
		global rp0State
		rp0State = 4
		await asyncio.sleep(0.01)
		await self.Moving2()

	async def Moving1(self):
		global rp0State
		rp0State = 3
		await asyncio.sleep(0.01)
		await self.Turning2()

	async def Turning1(self):
		global rp0State
		rp0State = 2
		await asyncio.sleep(0.01)
		await self.Moving1()

	async def Undock(self):
		global rp0State
		rp0State = 1
		await asyncio.sleep(0.01)
		await self.Turning1()

	async def Initalized(self):
		global rp0On
		rp0On = True
		await asyncio.sleep(0.01)
		await self.Undock()

class RaspberryPi1:
	def __init__(self, ):
		global CC
		global Pi0
		self.piNum = 1

	async def Initalized(self):
		global rp1On
		rp1On = True
		await asyncio.sleep(0.01)
		await self.Undock()

	async def Scanning2(self):
		global rp1State
		rp1State = 12
		await asyncio.sleep(0.01)
		await self.Mapping2()

	async def Moving4(self):
		global rp1State
		rp1State = 11
		await asyncio.sleep(0.01)
		await self.Scanning2()

	async def Turning4(self):
		global rp1State
		rp1State = 10
		await asyncio.sleep(0.01)
		await self.Moving4()

	async def Moving3(self):
		global rp1State
		rp1State = 9
		await asyncio.sleep(0.01)
		await self.Turning4()

	async def Mapping1(self):
		global rp1State
		rp1State = 8
		await asyncio.sleep(0.01)
		await self.Moving3()

	async def Scanning1(self):
		global rp1State
		rp1State = 7
		await asyncio.sleep(0.01)
		await self.Mapping1()

	async def Turning3(self):
		global rp1State
		rp1State = 6
		await asyncio.sleep(0.01)
		await self.Scanning1()

	async def Moving2(self):
		global rp1State
		rp1State = 5
		await asyncio.sleep(0.01)
		await self.Turning3()

	async def Turning2(self):
		global rp1State
		rp1State = 4
		await asyncio.sleep(0.01)
		await self.Moving2()

	async def Moving1(self):
		global rp1State
		rp1State = 3
		await asyncio.sleep(0.01)
		await self.Turning2()

	async def Turning1(self):
		global rp1State
		rp1State = 2
		await asyncio.sleep(0.01)
		await self.Moving1()

	async def Undock(self):
		global rp1State
		rp1State = 1
		await asyncio.sleep(0.01)
		await self.Turning1()

	async def Disconnecting(self):
		global rp1State
		rp1State = 0
		await asyncio.sleep(0.01)
		await self.Undock()

	async def Docking(self):
		global rp1State
		rp1State = 15
		await asyncio.sleep(0.01)
		await self.Disconnecting()

	async def Turning5(self):
		global rp1State
		rp1State = 14
		await asyncio.sleep(0.01)
		await self.Docking()

	async def Mapping2(self):
		global rp1State
		rp1State = 13
		await asyncio.sleep(0.01)
		await self.Turning5()

loop = asyncio.get_event_loop()
Pi0 = RaspberryPi0()
Pi1 = RaspberryPi1()
CC = CentralController(Pi0,  Pi1)
loop.run_until_complete(CC.Com_initialized())
loop.run_until_complete(Pi0.Initalized())
loop.run_until_complete(Pi1.Initalized())
