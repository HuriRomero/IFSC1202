num_even = 1
element = -1

while element != 0:
    element = int(input("Enter a Number (zero to quit): "))
if element % 2 == 0:
    num_even += 1
    print(num_even)