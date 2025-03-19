#Checks if a number is prime or not

Prime_Number = True
Inserted_Number = int (input("say a number: ")) 
if Inserted_Number == 2:
    print (Inserted_Number,"is prime")
#^ Ignores 2
elif Inserted_Number == 1:
    print (Inserted_Number,"is prime")
#^ Ignores 1        
elif Inserted_Number <= 0:
    print (Inserted_Number," is not a valid awser")
#^ Ignores 0 and negatives      
else:
   for a in range (2, Inserted_Number):
        if Inserted_Number % a == 0:
            print (Inserted_Number, "is not prime, divisible by: ", a)
            Prime_Number = False
            #^ Tells the divisible numbers and checks 'Prime_Number' as 'False'
        else:
            if Prime_Number == True: 
                print (Inserted_Number, " is prime")
                break
            #^ If 'Prime_Number' is 'True', prints the thing and breaks the loop