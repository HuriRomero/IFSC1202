result = 0 

N = int(input("Enter Number of Cards: "))
card = N 
for i in range (N - 1):
    N=int(input("Enter card: "))
    result += N
for i in range(card):
  card += i
i+=N
card -= result
print(card)




