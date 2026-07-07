def greet():
    print("Hello , Good Morning")

greet()

def printname(name):
    print("My name is :" +name)

printname("Santhosh")

def emplyee(name: str, empId: int , department: str):
    print("Name of Employee is " +name)
    print("Employee ID is " ,empId)
    print("Department is " +department)

emplyee("Santhosh", 123123, "Information technology")

def demoagrs(*number):
    print(number)
demoagrs(6,20,7,9,"name")