from weakref import finalize

class A:
    def __init__(self, ename):
        self.name = ename
        print(f"I am {self.name}")
    
    def method(self):
        print(f" {self.name} is gone")

res = A("Rohit")
finalize(res, res.method)

del res
