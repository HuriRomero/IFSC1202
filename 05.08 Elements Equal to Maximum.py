largest= 0
occurrences= 0
firstnumber= True
while True:
    num= int(input("Enter a Number (zero to quit): "))
    if firstnumber or largest< num:
        largest= num
        occurrences = 1
    elif largest == num:
        occurrences+= 1
    firstnumber = False
print("Maximum: ", largest)
print("Number of Occurrences: ", occurrences)
