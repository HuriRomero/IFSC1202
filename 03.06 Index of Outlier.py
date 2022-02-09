a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
c = int(input("Enter third Number: "))

if a == b and b == c:
    print("3")
elif a != b or  b != c or a != c:
    print("2")
else:
    print("1")