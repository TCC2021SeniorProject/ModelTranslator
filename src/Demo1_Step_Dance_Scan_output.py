import asyncio
import time

numLoops = 0
initalize = None #Channel variable
undock = None #Channel variable
dock = None #Channel variable
move = None #Channel variable
scan = None #Channel variable
disconnect = None #Channel variable
rp0Turn = None #Channel variable
rp1Turn = None #Channel variable
rp0Angle = 0.0
rp1Angle = 0.0
rp0Distance = 0.0
rp1Distance = 0.0
rp0ScanNum = 0
rp1ScanNum = 0
mapRp0 = 0
mapRp1 = 0

class CentralController:
	def __init__(self, ):
		global Pi0
		global Pi1
		self.numTurns = 0
		self.numLoops = 0

	async def Com_finished(self):
		pass

	async def Com_disconnect(self):
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Disconnecting(), Pi1.Disconnecting(), )
		await self.Com_finished()

	async def Com_move2(self):
		if (self.numTurns % 2 == False) and self.numTurns < 36:
			global rp0Angle
			rp0Angle = 10.0
			await asyncio.sleep(0.01)
			await asyncio.gather(Pi0.Turning(), )
			await self.Com_turn2()
		if (self.numTurns % 2 == True) and self.numTurns < 36:
			global rp1Angle
			rp1Angle = - 10.0
			await asyncio.sleep(0.01)
			await asyncio.gather(Pi1.Turning(), )
			await self.Com_turn2()
		if self.numTurns >= 36:
			self.numTurns = 0
			global rp0Distance
			rp0Distance = 1.0
			global rp1Distance
			rp1Distance = 1.0
			await asyncio.sleep(0.01)
			await asyncio.gather(Pi0.Moving(), Pi1.Moving(), )
			await self.Com_disconnect()

	async def Com_turn2(self):
		self.numTurns = self.numTurns + 1
		await asyncio.sleep(0.01)
		await self.Com_move2()

	async def Com_scan1(self):
		global rp0ScanNum
		rp0ScanNum = 25
		global rp1ScanNum
		rp1ScanNum = 25
		global mapRp0
		mapRp0 = self.numLoops + 1
		global mapRp1
		mapRp1 = self.numLoops + 1
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Scanning(), Pi1.Scanning(), )
		await self.Com_turn2()

	async def Com_move1(self):
		if self.numTurns >= 36:
			self.numTurns = 0
			global rp0Distance
			rp0Distance = 1.0
			global rp1Distance
			rp1Distance = 1.0
			await asyncio.sleep(0.01)
			await asyncio.gather(Pi0.Moving(), Pi1.Moving(), )
			await self.Com_scan1()
		if (self.numTurns % 2 == False) and self.numTurns < 36:
			global rp0Angle
			rp0Angle = - 10.0
			await asyncio.sleep(0.01)
			await asyncio.gather(Pi0.Turning(), )
			await self.Com_turn1()
		if (self.numTurns % 2 == True) and self.numTurns < 36:
			global rp1Angle
			rp1Angle = 10.0
			await asyncio.sleep(0.01)
			await asyncio.gather(Pi1.Turning(), )
			await self.Com_turn1()

	async def Com_turn1(self):
		self.numTurns = self.numTurns + 1
		await asyncio.sleep(0.01)
		await self.Com_move1()

	async def Com_initialized(self):
		await asyncio.sleep(0.01)
		await asyncio.gather(Pi0.Initializing(), Pi1.Initializing(), )
		await self.Com_turn1()

class RaspberryPi0:
	def __init__(self, ):
		global CC
		global Pi1
		self.piNum = 0

	async def Initialized(self):
		pass

	async def Initializing(self):
		await asyncio.sleep(0.01)
		await self.Initialized()

	async def Moved(self):
		pass

	async def Moving(self):
		await asyncio.sleep(0.01)
		await self.Moved()

	async def Disconnected(self):
		pass

	async def Disconnecting(self):
		await asyncio.sleep(0.01)
		await self.Disconnected()

	async def Scanned(self):
		pass

	async def Scanning(self):
		await asyncio.sleep(0.01)
		await self.Scanned()

	async def Turned(self):
		pass

	async def Turning(self):
		await asyncio.sleep(0.01)
		await self.Turned()

class RaspberryPi1:
	def __init__(self, ):
		global CC
		global Pi0
		self.piNum = 1

	async def Initialized(self):
		pass

	async def Initializing(self):
		await asyncio.sleep(0.01)
		await self.Initialized()

	async def Moved(self):
		pass

	async def Moving(self):
		await asyncio.sleep(0.01)
		await self.Moved()

	async def Disconnected(self):
		pass

	async def Disconnecting(self):
		await asyncio.sleep(0.01)
		await self.Disconnected()

	async def Scanned(self):
		pass

	async def Scanning(self):
		await asyncio.sleep(0.01)
		await self.Scanned()

	async def Turned(self):
		pass

	async def Turning(self):
		await asyncio.sleep(0.01)
		await self.Turned()

loop = asyncio.get_event_loop()
Pi0 = RaspberryPi0()
Pi1 = RaspberryPi1()
CC = CentralController()
loop.run_until_complete(CC.Com_initialized())
loop.run_until_complete(Pi0.Initializing())
loop.run_until_complete(Pi1.Initializing())
