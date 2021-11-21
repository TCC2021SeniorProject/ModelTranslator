status = 0
battery = 0

class all_tran_example:
	def __init__(self, status, battery):
		self.status = status
		self.battery = battery

	async def Dock(self):
		self.status = 0
		await self.Idle()

	async def Run(self):
		if self.status == 4 or self.battery < 10:
			await self.Dock()

	async def Idle(self):
		if self.status == 1 and self.battery > 10:
			await self.Run()

class clean:
	def __init__(self, ):
		pass

	async def Clean(self):
		exit()

	async def ShouldClean(self):
		if self.status == 3:
			await self.Clean()

class explore:
	def __init__(self, ):
		pass

	async def Explore(self):
		exit()

	async def ShouldExplore(self):
		if self.status == 2:
			await self.Explore()

Roomba = all_tran_example(status, battery)

Roomba.Idle()

