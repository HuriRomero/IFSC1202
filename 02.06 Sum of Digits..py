x = int(input("Enter a Number: "))

ones = (x % 10)
tens = (x % 100) // 10
hundreds =(x % 1000) // 100

print(ones + tens + hundreds)

