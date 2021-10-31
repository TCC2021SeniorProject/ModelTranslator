class TestClass:

	def __init__(self, ):
		print('Running constructor')
		self.status1 = 0
		self.charge1 = 0

	async def Dead(self):
		exit()

	async def Dock(self):
		if self.battery == 0 :
			self.mode = -1
			await self.Dead()
		if self.mode == 3 :
			await self.Clean()
		if self.mode == 2 :
			await self.Explore()
		self.mode = 0
		await self.Idle()


	async def Explore(self):
		if self.mode == 1 :
			await self.Ready()
		if self.mode == 4 or self.battery < 10 :
			self.mode = 4
			await self.Dock()
		if self.mode == 3 :
			await self.Clean()


	async def Clean(self):
		if self.mode == 1 :
			await self.Ready()
		if self.mode == 4 or self.battery < 10 :
			self.mode = 4
			await self.Dock()


	async def Ready(self):
		if self.mode == 0 or self.battery <= 10 :
			self.mode = 0
			await self.Idle()
		if self.mode == 1 :
			await self.Ready()
		if self.mode == 3 :
			await self.Clean()
		if self.mode == 2 :
			await self.Explore()


	async def Idle(self):
		if self.battery > 10 and self.mode == 1 :
			await self.Ready()



TestClass.Idle()
