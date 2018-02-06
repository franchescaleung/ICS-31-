'''
ICS 31 Winter 2018 Lecture 5 January 19




'''
def double(number: int) -> int:
    '''Takes an integer and returns its double'''
    return number * 2

assert double(2) == 4
assert double(0) == 0
assert double(-111) == -222

print (double(1 + 1))
print(double ("HO ")) #python doesn't care that we said we will work with numbers

'''FUNCTIONS
SYNTAX of a FUNCTION DEFINITION
def NAME (VAR: TYPE) -> TYPE:

    """DOCSTRING COMMENT:
        ONE LINE to DESCRIBE WHAT THE FUNCTION DOES"""
        Statement(s)
        return VALUE

assert statements


## Print vs Return
##Print is for user to see
##Return is for the program to use

'''
        
def sum_of_doubles(number1: int, number2: int) -> int:
    '''Take two numbers, double and sum them'''
    sum = number1 * 2 + number2 * 2
    return sum
assert sum_of_doubles(3, 10) == 26
assert sum_of_doubles(0, 0) == 0
assert sum_of_doubles(-1, -1000) == -2002

def mult (number:int, multiplier:int) -> int:

    

print ("sum of doubles for ", 2, "and", 3, "is", sum_of_doubles(2, 3))
