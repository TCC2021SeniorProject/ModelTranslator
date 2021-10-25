class TestClass:

	def __init__(self, ):
		print('Running constructor')
		self.status1 = 0
		self.charge1 = 0
		self.status2 = 0
		self.charge2 = 0
		self.status3 = 0
		self.charge3 = 0

	async def End(self):
		exit()

	async def Dock(self):
		await self.Ready()
		await self.End()

	async def Explore(self):
		if self.mode == 4 or self.battery < 10 :
			self.mode = 4
			await self.Dock()
		if self.mode == 3 :
			await self.Clean()


	async def Clean(self):
		if self.mode == 4 or self.battery < 10 :
			self.mode = 4
			await self.Dock()


	async def Ready(self):
		if self.mode == 3 :
			await self.Clean()
		if self.mode == 2 :
			await self.Explore()


	async def Idle(self):
		if self.battery > 10 and self.mode == 1 :
			await self.Ready()


	async def Start(self):
		self.mode = 1
		await self.Idle()


TestClass.Start()
