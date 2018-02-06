'''
ICS 31 Winter 2018 Irene Gassko
Lecture 3 January 12, 2018
'''
##TAX_RATE = 0.08
###compute total bill with a tip and a tax
##print("How big is the damage?")
##cost = float(input())
###tip_percent = 20
##tip_percent = int(input("How big a tip do you want to give?"))
##tip = cost * tip_percent/100
##tax = cost * TAX_RATE
##total = cost + tip + tax
##print("Total cost $", total)


#ASSIGNMENT
#SYNTAX variable = expression
#numbers +, -, *, /, % (mod/remainder), // interger division div --> gives integer
#strings + concatenation, * repetition

#Objects can have types int, float, str, boolean
##print(2 * 2 > 5)
##print (2 * 2 == 5 - 1)
### =: assignment Pascal
##
##done = True
##nice = False
##
##print (done and nice)
##print (done or nice)

##TAX_RATE = 0.08
###compute total bill with a tip and a tax
##print("How big is the damage?")
##cost = float(input())
###tip_percent = 20
##tip_percent = int(input("How big a tip do you want to give?"))
##tip = cost * tip_percent/100
##tax = cost * TAX_RATE
##total = cost + tip + tax
##print("Total cost $", total)

##functions
##int(), input(), float(), str()
##print()

#Methods
#Like functions, but syntax is different

#Lists
##temps = [33, 44, 55, 66, 77]
##print (temps[1])
##print (len(temps))
##
##days = ["Mon", "Tue"]
###use double quotes
##greeting = 'How\'s life' #use \ to let ' stay
##print (greeting)
##print (greeting, "\\") #only prints one \

#name tupple?
From collections import namedtuples
Student = namedtupel ("Student name", "ID", "major", "GPA")
s1 = Students ("Peter Anteater", 1111111, "ICS", 5.0)
print("GPA of me", s1.GPA)

