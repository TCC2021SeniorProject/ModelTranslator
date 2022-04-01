import asyncio
import time

connection = None #Channel variable
initalize = None #Channel variable
dance = None #Channel variable
dock = None #Channel variable
request = 0

class Template1:
    def __init__(self):
        pass

    async def print(self):
        print("before")
        task1 = loop.create_task(Template2().printOne())
        task2 = loop.create_task(Template2().printOne())

        await asyncio.wait([task1, task2])

        await Template2().printOne()
        await Template2().printOne()
        print("after")

class Template2:
    def __init__(self):
        pass
    async def printOne(self):
        await asyncio.sleep(0.01)
        print("One")
        await self.printTwo()

    async def printTwo(self):
        await asyncio.sleep(0.01)
        print("Sleep...")
        time.sleep(2)
        print("Two")

loop = asyncio.get_event_loop()
teml1 = Template1()
teml2 = Template2()
loop.run_until_complete(teml1.print())
loop.close()
