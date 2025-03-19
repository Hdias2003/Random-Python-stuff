#Plays a guessing game with numbers

n = 24
N = 0 
B = 0 
while n != N:
    N = int (input("Guess witch number i'm thinking of "))
    if n != N:
        print ("Wrong! Try again!") 
        B = B + 1
else:
    if B == 0:
        print ("Ok, cool, you got it first try")
    else:
        print ("hum ", B, "wrong guesses, kinda bad") 