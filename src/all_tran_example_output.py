import asyncio
import time

status = 0
battery = 0
check_mode = None #Channel variable

class all_tran_example:
	def __init__(self, mode, charge, ):
		self.mode = mode
		self.charge = charge

	async def Dock(self):
		global self.mode
		self.mode = 0
		await asyncio.sleep(0.01)
		await self.Idle()

	async def Run(self):
		if self.mode == 4 or self.charge < 10:
			await asyncio.sleep(0.01)
			await self.Dock()

	async def Idle(self):
		if self.mode == 1 and self.charge > 10:
			await asyncio.sleep(0.01)
			await self.Run()

class clean:
	def __init__(self, mode, ):
		global Roomba
		self.mode = mode

	async def default_init(self):
		if self.mode == 3:
			await asyncio.sleep(0.01)
			await asyncio.gather(Roomba.Idle(), )
			await self.Clean()

	async def Clean(self):
		pass

class explore:
	def __init__(self, mode, ):
		global Roomba
		self.mode = mode

	async def default_init(self):
		if self.mode == 2:
			await asyncio.sleep(0.01)
			await asyncio.gather(Roomba.Idle(), )
			await self.Explore()

	async def Explore(self):
		pass

loop = asyncio.get_event_loop()
Roomba = all_tran_example(status,  battery)
loop.run_until_complete(Roomba.Idle())
