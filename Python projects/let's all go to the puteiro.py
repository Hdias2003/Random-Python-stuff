#Goes to the brothel until there's no money left

Money = 1000
while Money >= 50:
    print  ("tenho ", Money, "euros, vamos ao puteiro!!")
    puta = input ("escolhe uma ")
    grana = float(input("? quanto q é essa ai? "))
    if Money >= grana:
        print ("comeu a ", puta, "e perdeu", grana)
        Money = Money - grana
    elif Money < grana:
        print ("sem money pra essa, brother. escolhe outra")
print ("só sobrou ", Money, "n é suficiente pra comer ninguem")
print ("o sonho acabou, hora de ir pra casa")