import asyncio

a = 5
b = 2

class test:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  async def calculate(self):
    await self.add()

  async def add(self):
    print("Printing")
    print(self.a + self.b)
    return

class test2:
    def __init__(self, a):
        self.a = a

    async def calculate(self):
        await test(a, b).add()

inst = test2(10)
#Use this on Python version lower than 3.7
loop = asyncio.get_event_loop()
loop.run_until_complete(inst.calculate())