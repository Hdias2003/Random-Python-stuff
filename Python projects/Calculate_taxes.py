#Simulates income based taxes

tax = float (input("annual income "))

if tax <= 85528:
    tax1 = ((tax * 0.18) - 556.02)
else:
    tax1 = (14839.02 + ((tax - 85528) * 0.32))
if tax1 < 0:
    tax1 = 0
print ("tax to be paid is:", round(tax1), "Euros")
print (((tax / 100) * 18) - 556.02)
