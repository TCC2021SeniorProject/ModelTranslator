import library1 # Idel(), Clean(), Dock()

class TestClass:
    def init(self, ):
        print('function generated')
        self.status1 = 0
        self.status2 = 0
        self.mode = 0


result = await Idel()
if (library1.battery > 10):
    result = await Clean()
    if (library1.mode == 2):
        result = await Clean()
            if (library1.mode == 3):
                result = await Clean()
                    if (library1.mode == 4):
                        result = await Dock()
            elif (library1.mode == 4):
                result = await Dock()
    elif (library1.mode == 3):
        result = await Clean()
        if (library1.mode == 4):
            result = await Dock()