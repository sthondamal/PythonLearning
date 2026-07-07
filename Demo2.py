values = [1, 4, "hello", 5.6]  #List in A Square braces

print(values[0])
print(values[-1])

print(values[0:6])

values.insert(3, "santhosh")
values.reverse()
print(values)

values.append("last")
print(values)

values[2] = "HELLO"
print(values)

del values[1]
print(values)

###Tuple - Immutable##

val = (2, 4.4, "happy", "new")

## Dictionary
val2= {"a": 2, 4: "Haooy", "b": "new value"}

print(val2["b"])

val3 = {}
val3["first_Name"] = "Santhosh"
val3["Last_Name"] = "Thondamal"

print(val3)

print(val3["Last_Name"])

