import asyncio

connection = None #Channel variable
initalize = None #Channel variable
dance = None #Channel variable
dock = None #Channel variable
request = 0

class MCCD:
	def __init__(self, connection, initalize, dance, dock, request, ):
		self.connection = connection
		self.initalize = initalize
		self.dance = dance
		self.dock = dock
		self.request = request

	async def com_dock(self):
		if self.request == 2:
			await self.com_init()

	async def com_dance(self):
		if self.request == 1:
			RasPi.Dancing()
			await self.com_dock()

	async def com_init(self):
		if self.request == 0 or self.request == 3:
			await self.com_dance()

	async def com_connect(self):
		RasPi.Idle()
		await self.com_init()

class RasPi:
	def __init__(self, connection, initalize, dance, dock, request, ):
		self.connection = connection
		self.initalize = initalize
		self.dance = dance
		self.dock = dock
		self.request = request

	async def Docking(self):
		self.request = 3
		
		MCCD.com_dock()
		await self.Initalized()

	async def Dancing(self):
		self.request = 2
		
		await self.Docking()

	async def Initalized(self):
		self.request = 1
		
		MCCD.com_init()
		await self.Dancing()

	async def Idle(self):
		self.request = 0
		
		await self.Initalized()

loop = asyncio.get_event_loop()
Laptop = MCCD(connection, initalize, dance, dock, request)
Pi = RasPi(connection, initalize, dance, dock, request)
loop.run_until_complete(Laptop.com_connect())
loop.run_until_complete(Pi.Idle())
