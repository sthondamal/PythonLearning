from OOPS.OppsDemo import Calculator

class childImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,2,3)

    def getFullData(self):
        return self.num2+self.num+self.summation()

obj = childImpl()
print(obj.getFullData())
