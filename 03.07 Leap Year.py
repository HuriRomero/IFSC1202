x = int(input("Enter year: "))

if x % 4 and x % 100 != 0 or x % 400 == 0:
    print("Leap Year")
else:
    print("Common Year")
    