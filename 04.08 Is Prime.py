N = int(input("Enter N: "))

if N > 1:
    for i in range(2, int(N / 2)+ 1):
        if (N % 1) == 0:
            print(N, "Composite")
            break
        else:
            print(N, "Prime")
else:
    print(N, Composite)