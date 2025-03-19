#Inputs the grades for all the tests and assingments of a course and calculates te averages

#PC_Fund 83.33/67.5/87.5/73.33
#Inter_SK 
#Prog_Esse
#UI_UX
#Numberology 52
#Core_SK 45

PCF_Test_1 = float (input ("Test 1 for Computer Fundamentals: "))
PCF_Test_2 = float (input ("Test 2 for Computer Fundamentals: "))
PCF_Test_3 = float (input ("Test 3 for Computer Fundamentals: "))
PCF_Test_4 = 0
PCF_Assing_1 = float (input ("Assing 1 for Computer Fundamentals: "))
PCF_Assing_2 = 0

IS_Present_1 = 0
IS_Present_2 = 0

PE_Test_1 = 0
PE_Test_2 = 0

UX_UI_Assing_1 = 0
UX_UI_Assing_2 = 0
UX_UI_Assing_3 = 0

N_Test_1 = float (input ("Test 1 for Numerology: "))
N_Test_2 = 0
N_Test_3 = 0

CS_Assing_1 = float (input ("Assingment 1 for Core Skills: "))
CS_Assing_2 = 0
CS_Assing_3 = 0
CS_Assing_4 = 0
CS_Assing_5 = 0
CS_Assing_6 = 0

PC_Fund_1 = ((PCF_Test_1 * 10) + (PCF_Test_2 * 10) + (PCF_Test_3 * 10) + (PCF_Test_4 * 10) + (PCF_Assing_1 * 30) + (PCF_Assing_2 * 30)) / 30
#Add 10, 30, 30
IS_1 = (IS_Present_1 * 40) + (IS_Present_2 * 60)  / 40
#Add 60
PE_1 = ((PE_Test_1 * 40) + (PE_Test_2 * 60)) / 40
#Add 60
UX_UI = (UX_UI_Assing_1 * 20) + (UX_UI_Assing_2 * 20) + (UX_UI_Assing_3 * 60)/ 20
#Add 20, 60
N_1 = ((N_Test_1 * 30) + (N_Test_2 * 30)+ (N_Test_3 * 40)) / 30
#add 30, 40
CS_1 = ((CS_Assing_1 * 10) + (CS_Assing_2 * 10) + (CS_Assing_3 * 20)  + (CS_Assing_4 * 20)  + (CS_Assing_5 * 20)  + (CS_Assing_6 * 20)) / 10
#add 10, 20, 20, 20, 20

print  ("\n \n___Preliminary grades___ \n \n", "Computer Fundamentals - ", round(PC_Fund_1, 2), "\n Interpesonal Skills - ", round(IS_1, 2), "\n Programming Essencials - ", round(PE_1, 2), "\n UX and UI - ", round(UX_UI, 2), "\n Numerology - ", round(N_1, 2), "\n Core Skills - ", round(CS_1, 2), "\n")

if PC_Fund_1 < 40:
    print ("\n Bad news on Computer Fundamentals")
if IS_1 < 40:
    print ("\n Bad news on Interpesonal Skills")
if PE_1 < 40:
    print ("\n Bad news on programing essencials")
if UX_UI < 40:
    print ("\n Bad news on UI & UX")
if N_1 < 40:
    print ("\n Bad news on numerologia")
if CS_1 < 40:
    print ("\n Bad news on Core Skills")               
Todas = (PC_Fund_1 + IS_1 + PE_1 + UX_UI + N_1 + CS_1) / 6
if Todas >= 40:
    print ("\nAll grades good, for now...")