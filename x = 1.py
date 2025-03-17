n = 11
N = 0 
B = 0 
while n != N:
    N = int (input("What's the number? 1 to 10 "))
    if n != N:
        print ("Wrong! Moron!") 
        B = B + 1
else:
    if B == 0:
        print ("congrats, you got it rigth first try")
    else:
        print ("ok, you got it right, but you're still a moron, you had", B, "wrong guesses") 