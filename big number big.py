X = int (input("first ")) 
Y = int (input("second ")) 
Z = int (input("thrid "))
W = int (input("forth "))
B = int (input("fifth "))
if X > Y:
    A = X
else:
    A = Y
if A > Z:
    big = A
else:
    big = Z
if big > W:
    big2 = big
else:
    big2 = W
if big2 > B:
    big3 = big2
else:
    big3 = B

#Second definition
print ("big number is ", big3)