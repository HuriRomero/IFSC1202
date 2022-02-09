x = int(input("Enter a Number: "))

ones = x % 10
tens = (x // 10) % 10
hundreds = (x // 100) % 10
thousands = (x // 1000) % 10
if ones == thousands and tens == hundreds:
    print("yes")
else:
    print("no")