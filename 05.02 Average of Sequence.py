S = 0
n = 0
a = int(input("Enter a Number (zero to quit): "))
while a != 0:
    S += a
    n += 1
    a = int(input("Sequence Length is "))
print("Average: ",S/n)