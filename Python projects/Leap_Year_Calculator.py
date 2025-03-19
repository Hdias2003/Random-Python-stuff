#Calculates a leap year 

Year = int (input("Say the year: "))
if Year <= 1582:
    print ("Not within the Gregorian Calendar")
elif Year % 4 != 0:
    print ("Regular year")
elif Year % 100 != 0: 
    print ("Leap year")
elif Year % 400 != 0:
    print ("Regular Year")
else:
    print ("Regular year")        