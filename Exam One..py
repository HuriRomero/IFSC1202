from random import randint

N = (input("Hello! What is your name? "))
print("Well, Joe, I am thinking of a number between 1 and 20. ")
print("You have 5 guesses. ")
x = randint(1, 20) 
for i in range (5):
    a = int(input("Take a Guess: "))
    if (a > x):
        print("Your guess is too high. ")
    elif(a < x): 
         print("Your guess is too low. ")
    elif(a == i):
        x == 7
        print("Good job, Joe! You guessed my number in 3 guesses! ")
    else:
        a =  x != 11
        print("Nope. The number I was thinking of was 11 ")