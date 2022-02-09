x = int(input("Enter First 2 Digit Number: "))
y = int(input("Enter Second 2 Digit Number: "))
onesdigits = x % 10
tensdigit = x // 10
secondonesdigit = y % 10
secondtensdigit = y // 10

print("Merged Number: ", onesdigits,secondonesdigit,tensdigit,secondtensdigit)