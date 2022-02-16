S = 0
a = int(input("Enter a Number (zero to quit): "))

while a != 0:
    S += a
    a = int(input("Enter a Number (zero to quit): "))
print("Sum: ", S)