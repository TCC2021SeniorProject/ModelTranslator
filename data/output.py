status = 0
battery = 0
check_mode = None #Channel variable

class all_tran_example:
	def __init__(self, status, battery, ):
		self.status = status
		self.battery = battery

	async def Dock(self):
		await self.Idle()

	async def Run(self):
		if mode == 4 or charge < 10:
			await self.Dock()

	async def Idle(self):
		if mode == 1 and charge > 10:
			await self.Run()

class clean:
	def __init__(self, ):
		pass

	async def Clean(self):
		exit()

	async def default_init(self):
		if mode == 3:
			all_tran_example().Run()
			await self.Clean()

class explore:
	def __init__(self, ):
		pass

	async def Explore(self):
		exit()

	async def default_init(self):
		if mode == 2:
			all_tran_example().Run()
			await self.Explore()

Roomba = all_tran_example(status, battery)

Roomba.Idle()

