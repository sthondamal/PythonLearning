fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("First Fruit: " + fruits[0])
print("Last Fruit: " + fruits[-1])
print("Fruits from index 1 to 2: " + str(fruits[1:3]))

#######################

person = ("Rahul", 25, 5.9)
print("Age: " + str(person[1]))
print("Age:", person[1])

#############
car = {"make": "Toyota",

       "model": "Camry",

       "year": 2020,

       "color": "Blue"}

print("Car model: " + car["model"])

car["owner"] = "Rahul"

print("Updated car dictionary: ", car)

