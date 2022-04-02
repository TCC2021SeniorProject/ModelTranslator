import asyncio

connection = None #Channel variable
initalize = None #Channel variable
dance = None #Channel variable
disconnect = None #Channel variable
dock = None #Channel variable
request = 0

class MCCD:
	def __init__(self, connection, initalize, dance, dock, disconnect, request, ):
		self.connection = connection
		self.initalize = initalize
		self.dance = dance
		self.dock = dock
		self.disconnect = disconnect
		self.request = request
		self.numLoops = 0

	async def com_disconnect(self):
		await asyncio.sleep(0.01)
		if self.request == 3:
			Disconnecting_task_0 = loop.create_task(RasPi0.Disconnecting())
			Disconnecting_task_1 = loop.create_task(RasPi1.Disconnecting())
		await asyncio.wait([Disconnecting_task_0, Disconnecting_task_1, ])
			await self.com_init()

	async def com_dock(self):
		await asyncio.sleep(0.01)
		if self.request == 2:
			await self.com_disconnect()

	async def com_dance(self):
		await asyncio.sleep(0.01)
		if self.request == 1:
			Dancing0_task_0 = loop.create_task(RasPi0.Dancing0())
			Dancing1_task_1 = loop.create_task(RasPi1.Dancing1())
		await asyncio.wait([Dancing0_task_0, Dancing1_task_1, ])
			await self.com_dock()

	async def com_init(self):
		await asyncio.sleep(0.01)
		if self.request == 0 and numLoops < 2:
			await self.com_dance()

	async def com_connect(self):
		await asyncio.sleep(0.01)
		Idle_task_0 = loop.create_task(RasPi0.Idle())
		Idle_task_1 = loop.create_task(RasPi1.Idle())
		await asyncio.wait([Idle_task_0, Idle_task_1, ])
	await self.com_init()

class RasPi0:
	def __init__(self, connection, initalize, dance, dock, disconnect, request, ):
		self.connection = connection
		self.initalize = initalize
		self.dance = dance
		self.dock = dock
		self.disconnect = disconnect
		self.request = request
		self.piNum = 0

	async def Disconnecting(self):
		await asyncio.sleep(0.01)
		self.request = 0
		
		await self.Initalized()

	async def Docking(self):
		await asyncio.sleep(0.01)
		self.request = 3
		
		com_dock_task_0 = loop.create_task(MCCD.com_dock())
		await asyncio.wait([com_dock_task_0, ])
		await self.Disconnecting()

	async def Dancing0(self):
		await asyncio.sleep(0.01)
		self.request = 2
		
		await self.Docking()

	async def Initalized(self):
		await asyncio.sleep(0.01)
		self.request = 1
		
		com_init_task_0 = loop.create_task(MCCD.com_init())
		await asyncio.wait([com_init_task_0, ])
		await self.Dancing0()

	async def Idle(self):
		await asyncio.sleep(0.01)
		self.request = 0
		
		await self.Initalized()

class RasPi1:
	def __init__(self, connection, initalize, dance, dock, disconnect, request, ):
		self.connection = connection
		self.initalize = initalize
		self.dance = dance
		self.dock = dock
		self.disconnect = disconnect
		self.request = request
		self.piNum = 1

	async def Disconnecting(self):
		await asyncio.sleep(0.01)
		self.request = 0
		
		await self.Initalized()

	async def Docking(self):
		await asyncio.sleep(0.01)
		self.request = 3
		
		com_dock_task_0 = loop.create_task(MCCD.com_dock())
		await asyncio.wait([com_dock_task_0, ])
		await self.Disconnecting()

	async def Dancing1(self):
		await asyncio.sleep(0.01)
		self.request = 2
		
		await self.Docking()

	async def Initalized(self):
		await asyncio.sleep(0.01)
		self.request = 1
		
		com_init_task_0 = loop.create_task(MCCD.com_init())
		await asyncio.wait([com_init_task_0, ])
		await self.Dancing1()

	async def Idle(self):
		await asyncio.sleep(0.01)
		self.request = 0
		
		await self.Initalized()

loop = asyncio.get_event_loop()
Pi0 = RasPi0(connection, initalize, dance, dock, disconnect, request)
Pi1 = RasPi1(connection, initalize, dance, dock, disconnect, request)
Laptop = MCCD(connection, initalize, dance, dock, disconnect, request)
loop.run_until_complete(Laptop.com_connect())
loop.run_until_complete(Pi0.Idle())
loop.run_until_complete(Pi1.Idle())
