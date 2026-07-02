#for i in range(7,71,7):
#     print(i)
#for i in range(1,11):
    #print(i*7)

#password
password = "password@123"
user = " "

while user !=password:
    user = input("Enter password:")

print("Access Granted")

#Write a program for ATM pin verification

AtmPin = 1234
pin = " "

while pin != AtmPin:
    pin = int(input("Enter Pin"))

print("Pin in correct")
