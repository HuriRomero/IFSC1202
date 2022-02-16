N= int(input("enter first number: "))
SN= int(input("enter second number: "))

if SN > N:
    N, SN= SN, N

num=int(input("enter a number (zero to quit): "))

while(num != 0 ): 
    if num > N:
        n, SN = num,N
    elif num > SN:
        SN = num
    num= int(input("enter a number (zero to quit): "))
print("first maximum: ", N)
print("second maximum: ", SN)
print("")