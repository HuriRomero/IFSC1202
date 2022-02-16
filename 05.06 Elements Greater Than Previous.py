x = int(input("Enter a Number (zero to quit): "))
lst = []
count = 0

while x != 0:
  lst.append(x)
  x = int(input("Enter a Number (zero to quit): "))

for i in range(1,len(lst)):
  if lst[i] > lst[i-1]:
    count += 1
    
print(count)