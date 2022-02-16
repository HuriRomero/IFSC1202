list1 = [0]
num = int(input("Enter a Number (zero to quit): "))

for i in range(1, num + 1):
    ele = int(input("Enter a Number (zero to quit): "))
    list1.append(ele)
print("maximum: ", max(list1))