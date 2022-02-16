highest= 0 
index= 0 
highest_index= 0
while True:
    num= int(input("enter a number (zero to quit): "))
    if(num==0): break
    index+=1
    if num>highest:
        highest,highest_index=num,index

print("maximum: {}".format(highest))
print("index of maximum: {}".format(highest_index))
