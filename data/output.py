status = 0
battery = 0
check_mode = None

class all_tran_example:
	def __init__(self, ):
		pass

	async def Dock(self):
		self.mode = 0
		await self.Idle()

	async def Run(self):
		if self.mode == 4 or self.charge < 10:
			await self.Dock()

	async def Idle(self):
		if self.mode == 1 and self.charge > 10:
			await self.Run()

class clean:
	def __init__(self, ):
		pass

	async def Clean(self):
		exit()

	async def default_init(self):
		if self.mode == 3:
			await self.Clean()

class explore:
	def __init__(self, ):
		pass

	async def Explore(self):
		exit()

	async def default_init(self):
		if self.mode == 2:
			await self.Explore()

Roomba = all_tran_example(status, battery)

Roomba.Idle()

