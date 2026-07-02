###
#Amount = int(input("Enter the Billing amount : "))

#if Amount>=5000:
#    print("Discount is 20%")
#elif Amount>=3000:
 #   print("Discount is 15%")
#elif Amount>=1000:
 #   print("Discount is 10%")
#elif Amount<=500:
  #  print("No Discount")
#/

num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the Second Number: "))
operator = input("Enter Operator (+,-,*,% ): 1")

if operator == '+' :
    print("Result :" , num1+num2)
elif operator == '-' :
    print("Result :" , num1-num2)
elif operator == '*' :
    print("Result :" , num1*num2)
elif operator == '*' :
    print("Result :" , num1%num2)
else :
    print("Invalid Operator")

######################################

greeting = input("Enter the value for greeting: ")
if greeting == "Hello":
    print("Hello there!")
    print("How can I assist you today?")
else:
    print("Greetings!")
print("Program has completed.")

######################################

b = 15

if b > 10:
    print("Number is greater than 10")
else:
    print("Number is 10 or less")
print("Comparison code is completed")

####################################

ary = [1, 4, 7, 10]

for x in ary:
    val = x * 3
    print(val)