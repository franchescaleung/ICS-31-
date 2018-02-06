##Lecture 7 ICS 31 Winter 2018

def is_leap_year (year: int) -> bool:
    if year % 400 == 0:
        is_leap = True
    elif year % 100 == 0:
            is_leap = False
    elif year % 4 == 0:
                is_leap = True
    else:
                is_leap = False
    return is_leap

done = False
while not done:
    year = int(input("Give me a year "))
    if year == 0:
        done = True
    else: 
        if is_leap_year (year):
            print("Year", year, "is a leap year")
        else:
            print("Year", year, "is not a leap year")
print("Done, thank you very much")

#WHILE LOOP SYNTAX
'''
while boolean-expression:
    STATEMENTS
#While loop semantics
Test the boolean expression
if it's true, do the body
if it's false, get out of the loop
