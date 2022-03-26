import asyncio

direct1 = 0
direct2 = 0
request1 = 0
request2 = 0

class roomba:
	def __init__(self, request, mode, ):
		self.request = request
		self.mode = mode

	async def Dancing(self):
		if self.mode == 1:
			await self.Initialized()

	async def Waiting(self):
		if self.mode == 3:
			await self.Dancing()

	async def Initialized(self):
		if self.mode == 2:
			await self.Waiting()

	async def Idle(self):
		if self.mode == 1:
			await self.Initialized()

class MCCD:
	def __init__(self, req1, req2, mode1, mode2, ):
		self.req1 = req1
		self.req2 = req2
		self.mode1 = mode1
		self.mode2 = mode2

	async def com_dock(self):
		if self.req1 == 4 or self.req2 == 4:
			await self.com_dance()
		if self.req1 == 2 and self.req2 == 2:
			await self.com_init()

	async def dancing1(self):
		self.mode1 = 1
		await self.com_dock()

	async def dancing2(self):
		self.mode2 = 1
		await self.com_dock()

	async def com_dance(self):
		if self.req2 == 4:
			await self.dancing2()
		if self.req1 == 4:
			await self.dancing1()

	async def check_init(self):
		if self.req1 == 1 and self.req2 == 1:
			await self.com_dance()

	async def com_init(self):
		self.mode1 = 1self.mode2 = 1
		await self.check_init()

loop = asyncio.get_event_loop()
Laptop = MCCD(request1, direct1, request2, direct2)
Roomba1 = roomba(request1, direct1)
Roomba2 = roomba(request2, direct2)
loop.run_until_complete(Laptop.com_init())
loop.run_until_complete(Roomba1.Idle())
loop.run_until_complete(Roomba2.Idle())
