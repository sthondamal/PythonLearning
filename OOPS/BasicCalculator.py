class BasicCalculator:
    num1 = 10
    num2 = 5

    def __init__(self, num1 , num2):
        self.firstNo = num1
        self.secondNo = num2

    def addition(self):
        return self.firstNo+self.secondNo

    def subtractio(self):
        return self.firstNo - self.secondNo

    def multiplication(self):
        return self.firstNo * self.secondNo

    def division(self):
        return self.firstNo/self.secondNo

obj = BasicCalculator(10, 5)
print("Addition: ", obj.addition())
print("Subtraction: ",obj.subtractio())
print("Multiplication: ",obj.multiplication())
print("Division: ",obj.division())
