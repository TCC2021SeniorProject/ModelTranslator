import asyncio
from pycreate2 import Create2


class Roomba_Instance:
	def __init__(self, ):
		self.keepDancing = 4

	async def Dock(self):

		global roomba
		roomba.close()

		exit()

	async def Forward(self):
		if self.keepDancing == 0:
			await self.Dock()
		if self.keepDancing != 0:
			await self.Right()

	async def Right(self):
		self.keepDancing = keepDancing -1
		await self.Forward()

	async def Backward(self):
		await self.Right()

	async def Ready(self):

		global roomba
		sensor = roomba.get_sensors()
		print("global roomba {sensor.battery_charge} / {sensor.battery_capacity} charged")

		await self.Backward()

	async def Connect(self):

		global roomba
		port = '/dev/ttyUSB0'
		print('Port set to \'/dev/ttyUSB0\'.')
		roomba = Create2(port)
		print('global roomba object created.')
		roomba.start()
		roomba.safe()
		print('global roomba set to safe mode.')

		await self.Ready()

loop = asyncio.get_event_loop()
Process = Roomba_Instance()
loop.run_until_complete(Process.Connect())
