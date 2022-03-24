import asyncio

status = 0
battery = 0
check_mode = None #Channel variable

class all_tran_example:
	def __init__(self, mode, charge, ):
		self.mode = mode
		self.charge = charge

	async def Dock(self):
		self.self.mode = 0
		await self.Idle()

	async def Run(self):
		if self.self.mode == 4 or self.charge < 10:
			await self.Dock()

	async def Idle(self):
		if self.self.mode == 1 and self.charge > 10:
			await self.Run()

class clean:
	def __init__(self, mode, ):
		self.mode = mode

	async def Clean(self):
		exit()

	async def default_init(self):
		if self.self.mode == 3:
			Roomba.Run()
			await self.Clean()

class explore:
	def __init__(self, mode, ):
		self.mode = mode

	async def Explore(self):
		exit()

	async def default_init(self):
		if self.self.mode == 2:
			Roomba.Run()
			await self.Explore()

loop = asyncio.get_event_loop()
Roomba = all_tran_example(status, battery)
Roomba = all_tran_example(status, battery)
Roomba = all_tran_example(status, battery)
Roomba = all_tran_example(status, battery)
loop.run_until_complete(Roomba.Idle())
