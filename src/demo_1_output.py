import asyncio
import time
from pycreate2 import Create2
import time


class Roomba_Instance:
	def __init__(self, ):
		self.keepDancing = 4

	async def Dock(self):
		global roomba

		pass

	async def Forward(self):
		if self.keepDancing == 0:
			await asyncio.sleep(0.01)
			await self.Dock()
		if self.keepDancing != 0:
			await asyncio.sleep(0.01)
			await self.Right()

	async def Right(self):
		self.keepDancing = keepDancing -1
		await asyncio.sleep(0.01)
		await self.Forward()

	async def Backward(self):
		await asyncio.sleep(0.01)
		await self.Right()

	async def Ready(self):
		global roomba
		sensor = roomba.get_sensors()
		print("global roomba {sensor.battery_charge} / {sensor.battery_capacity} charged")

		await asyncio.sleep(0.01)
		await self.Backward()

	async def Connect(self):
		global roomba
		# Serial port
		port = '/dev/ttyUSB0' #test comment
		print('Port set to \'/dev/ttyUSB0\'.')
		# global roomba object
		roomba = Create2(port)
		print('global roomba object created.')
		roomba.start()
		# Safe mode
		roomba.safe()
		print('global roomba set to safe mode.')

		await asyncio.sleep(0.01)
		await self.Ready()

loop = asyncio.get_event_loop()
Process = Roomba_Instance()
loop.run_until_complete(Process.Connect())
