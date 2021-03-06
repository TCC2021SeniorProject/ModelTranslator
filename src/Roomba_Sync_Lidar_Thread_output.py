import asyncio

initalize = None #Channel variable
undock = None #Channel variable
dock = None #Channel variable
disconnect = None #Channel variable
turn1 = None #Channel variable
turn2 = None #Channel variable
turn3 = None #Channel variable
turn4 = None #Channel variable
turn5 = None #Channel variable
move1 = None #Channel variable
move2 = None #Channel variable
move3 = None #Channel variable
move4 = None #Channel variable
move5 = None #Channel variable
rp0On = False
rp1On = False
rp0Angle = 0.0
rp0Distance = 0.0
rp1Angle = 0.0
rp1Distance = 0.0
scan1 = None #Channel variable
scan2 = None #Channel variable
map1 = None #Channel variable
map2 = None #Channel variable
rp0ScanTime = 0.0
rp1ScanTime = 0.0
map1Rp0 = 0
map1Rp1 = 0
map2Rp0 = 0
map2Rp1 = 0

class CentralController:
	def __init__(self, ):
		self.numLoops = 0

	async def Com_disconnect(self):
		await asyncio.sleep(0.01)
		self.numLoops = numLoops +1
		
		await self.Com_undock()

	async def Com_dock(self):
		await asyncio.sleep(0.01)
		await self.Com_disconnect()

	async def Com_turn5(self):
		await asyncio.sleep(0.01)
		rp0Angle = -90.0
		rp1Angle = 90.0
		
		await self.Com_dock()

	async def Com_map2(self):
		await asyncio.sleep(0.01)
		map2Rp0 = numLoops +1
		map2Rp1 = numLoops +1
		
		await self.Com_turn5()

	async def Com_scan2(self):
		await asyncio.sleep(0.01)
		rp0ScanTime = 2.0
		rp1ScanTime = 2.0
		
		await self.Com_map2()

	async def Com_move4(self):
		await asyncio.sleep(0.01)
		rp0Distance = 1.0
		rp1Distance = 1.0
		
		await self.Com_scan2()

	async def Com_turn4(self):
		await asyncio.sleep(0.01)
		rp0Angle = -90.0
		rp1Angle = 90.0
		
		await self.Com_move4()

	async def Com_move3(self):
		await asyncio.sleep(0.01)
		rp0Distance = 1.0
		rp1Distance = 1.0
		
		await self.Com_turn4()

	async def Com_map1(self):
		await asyncio.sleep(0.01)
		map1Rp0 = numLoops +1
		map1Rp1 = numLoops +1
		
		await self.Com_move3()

	async def Com_scan1(self):
		await asyncio.sleep(0.01)
		rp0ScanTime = 1.0
		rp1ScanTime = 1.0
		
		await self.Com_map1()

	async def Com_turn3(self):
		await asyncio.sleep(0.01)
		rp0Angle = 90.0
		rp1Angle = -90.0
		
		await self.Com_scan1()

	async def Com_move2(self):
		await asyncio.sleep(0.01)
		rp0Distance = 1.0
		rp1Distance = 1.0
		
		await self.Com_turn3()

	async def Com_turn2(self):
		await asyncio.sleep(0.01)
		rp0Angle = 90.0
		rp1Angle = -90.0
		
		await self.Com_move2()

	async def Com_move1(self):
		await asyncio.sleep(0.01)
		rp0Distance = 1.0
		rp1Distance = 1.0
		
		await self.Com_turn2()

	async def Com_turn1(self):
		await asyncio.sleep(0.01)
		rp0Angle = 180.0
		rp1Angle = -180.0
		
		await self.Com_move1()

	async def Com_undock(self):
		await asyncio.sleep(0.01)
		rp0Distance = -0.1
		rp1Distance = -0.1
		
		await self.Com_turn1()

	async def Com_initialized(self):
		await asyncio.sleep(0.01)
		Initalized_task_0 = loop.create_task(RaspberryPi0().Initalized())
		Initalized_task_1 = loop.create_task(RaspberryPi1().Initalized())
		await asyncio.wait([Initalized_task_0, Initalized_task_1, ])
		await self.Com_undock()

class RaspberryPi0:
	def __init__(self, ):
		self.piNum = 0

	async def Disconnecting(self):
		await asyncio.sleep(0.01)
		await self.Undock()

	async def Docking(self):
		await asyncio.sleep(0.01)
		await self.Disconnecting()

	async def Turning5(self):
		await asyncio.sleep(0.01)
		await self.Docking()

	async def Mapping2(self):
		await asyncio.sleep(0.01)
		await self.Turning5()

	async def Scanning2(self):
		await asyncio.sleep(0.01)
		await self.Mapping2()

	async def Moving4(self):
		await asyncio.sleep(0.01)
		await self.Scanning2()

	async def Turning4(self):
		await asyncio.sleep(0.01)
		await self.Moving4()

	async def Moving3(self):
		await asyncio.sleep(0.01)
		await self.Turning4()

	async def Mapping1(self):
		await asyncio.sleep(0.01)
		await self.Moving3()

	async def Scanning1(self):
		await asyncio.sleep(0.01)
		await self.Mapping1()

	async def Turning3(self):
		await asyncio.sleep(0.01)
		await self.Scanning1()

	async def Moving2(self):
		await asyncio.sleep(0.01)
		await self.Turning3()

	async def Turning2(self):
		await asyncio.sleep(0.01)
		await self.Moving2()

	async def Moving1(self):
		await asyncio.sleep(0.01)
		await self.Turning2()

	async def Turning1(self):
		await asyncio.sleep(0.01)
		await self.Moving1()

	async def Undock(self):
		await asyncio.sleep(0.01)
		if rp0On == True:
			await self.Turning1()

	async def Initalized(self):
		await asyncio.sleep(0.01)
		rp0On = True
		
		await self.Undock()

class RaspberryPi1:
	def __init__(self, ):
		self.piNum = 1

	async def Disconnecting(self):
		await asyncio.sleep(0.01)
		await self.Undock()

	async def Docking(self):
		await asyncio.sleep(0.01)
		await self.Disconnecting()

	async def Turning5(self):
		await asyncio.sleep(0.01)
		await self.Docking()

	async def Mapping2(self):
		await asyncio.sleep(0.01)
		await self.Turning5()

	async def Scanning2(self):
		await asyncio.sleep(0.01)
		await self.Mapping2()

	async def Moving4(self):
		await asyncio.sleep(0.01)
		await self.Scanning2()

	async def Turning4(self):
		await asyncio.sleep(0.01)
		await self.Moving4()

	async def Moving3(self):
		await asyncio.sleep(0.01)
		await self.Turning4()

	async def Mapping1(self):
		await asyncio.sleep(0.01)
		await self.Moving3()

	async def Scanning1(self):
		await asyncio.sleep(0.01)
		await self.Mapping1()

	async def Turning3(self):
		await asyncio.sleep(0.01)
		await self.Scanning1()

	async def Moving2(self):
		await asyncio.sleep(0.01)
		await self.Turning3()

	async def Turning2(self):
		await asyncio.sleep(0.01)
		await self.Moving2()

	async def Moving1(self):
		await asyncio.sleep(0.01)
		await self.Turning2()

	async def Turning1(self):
		await asyncio.sleep(0.01)
		await self.Moving1()

	async def Undock(self):
		await asyncio.sleep(0.01)
		if rp1On == True:
			await self.Turning1()

	async def Initalized(self):
		await asyncio.sleep(0.01)
		rp1On = True
		
		await self.Undock()

loop = asyncio.get_event_loop()
Pi0 = RaspberryPi0()
Pi1 = RaspberryPi1()
CC = CentralController()
loop.run_until_complete(CC.Com_initialized())
loop.run_until_complete(Pi0.Initalized())
loop.run_until_complete(Pi1.Initalized())
