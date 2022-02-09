a = int(input("Enter point A: "))
b = int(input("Enter point B: "))
c = int(input("Enter point C: "))

dis1 = (a - b)
dis2 = (a - c)
if dis1 > dis2:
    print(dis2)
else:
    print(dis1)

