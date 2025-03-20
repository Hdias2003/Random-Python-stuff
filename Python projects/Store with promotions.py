# Checks for age and total money spend of a customer, and checks if they are elegible for discounts based on being under 18 and spending over 100 euros
# test data 1: First costumer age 12, total amount 300. Second costumer age 12, amount 50, third costumer age 20, total 50. No more customers
# Test data 2: First costumer age 21, total amount 100. Second costumer age 15, amount 190, Third costumer age 8, total 130. No more customers 

Age = int(input("Please enter your age: " ))
Amount = float(input("Please enter the price of the product (Euro): "))
Choise = "yes"
Discount = 0
Discounted_Amount = 0

while Choise == "yes":
    if Age <= 18:
        #Customer can apply for 10% discount
        Discount = (Amount * 0.10)
        Discounted_Amount = (Amount - Discount)
        if Discounted_Amount > 100:
            #Customer apply for 10 euro discount
            Discounted_Amount = (Discounted_Amount - 10)           
            print ("The final price is: ", Discounted_Amount)
            print ("You have earned: 10% discount and €10 promotion discount")
            Choise = (input("Would you like to enter another customer? (yes/no): "))
            if Choise == "no":
                #Ends the program
                break
        else:
            #Customer doesn't apply for 10 euro discount
            print ("The final price is: ", Discounted_Amount)
            print ("You have earned: 10% discount. ")
            Choise = (input("Would you like to enter another customer? (yes/no): "))
        if Choise == "no":
            #Ends the program
            break
        else:
            #Input another customer data
            Age = int(input("Please enter your age: " ))
            Amount = float(input("Please enter the price of the product (Euro): "))


    else: 
         #Customer doesn't apply for any discounts
        print ("The final price is: ", Amount, " Euro")
        print ("You have earned: No discounts or promotions.")
        Choise = (input("Would you like to enter another customer? (yes/no): "))
        if Choise == "no":
            #Ends the program
            break
        else:
            #Input another customer data
            Age = int(input("Please enter your age: " ))
            Amount = float(input("Please enter the price of the product (Euro): "))

