class TestClass:

	def __init__(self, ):
		print('Running constructor')
		self.status1 = 0
		self.charge1 = 0

	async def End(self):
		exit()

	async def Clean(self):
		if self.mode == 4 or self.battery < 10 :
			self.mode = 4
			await self.End()


	async def Ready(self):
		if self.mode == 3 :
			await self.Clean()


	async def Start(self):
		if self.mode == 1 and self.battery > 10 :
			await self.Ready()



TestClass.Start()
