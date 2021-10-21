class TestClass:

	def __init__(self, ):
		print('Running constructor')

	async def End():


	async def Dock():
		await End()

	async def Explore():
		if mode == 4 or battery < 10:
			await Dock()
		if mode == 3:
			await Clean()


	async def Clean():
		if mode == 4 or battery < 10:
			await Dock()


	async def Ready():
		if mode == 3:
			await Clean()
		if mode == 2:
			await Explore()


	async def Idle():
		if battery > 10 and mode == 1:
			await Ready()


	async def Start():
		await Idle()


