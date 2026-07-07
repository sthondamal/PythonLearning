class Calculator:
    num = 100

#default Constructor
    def __init__(self, a, b):
        self.firstNum=a;
        self.secondNum=b;
        print("Called automatically when obj is crated")

    def getData(self):
        print("As a method in the class")

    def summation(self):
        return self.firstNum + self.secondNum + self.num


obj = Calculator(2,3) #syntax to create variable
obj.getData()
obj.num
print(obj.summation())

obj1 = Calculator(3,4)
print(obj1.summation())







