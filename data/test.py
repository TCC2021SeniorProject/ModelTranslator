class A:
    def __init__(self):
        global instance_b1
        global instance_b2

    def incrementB(self):
        instance_b1.increment()
        instance_b1.increment()
        instance_b1.increment()
        instance_b2.increment()
        instance_b1.print()
        instance_b2.print()
    
class B:
    def __init__(self):
        self.local_var = 5

    def increment(self):
        self.local_var += 1

    def print(self):
        print(self.local_var)

instance_a = A()
instance_b1 = B()
instance_b2 = B()

instance_a.incrementB()
