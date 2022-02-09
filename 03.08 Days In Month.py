x = int(input("Enter month: "))

if x == (1, 3, 5, 7, 8, 10, 12):
    print("31")
elif x == 2:
    print("28")
else:
    print("30")