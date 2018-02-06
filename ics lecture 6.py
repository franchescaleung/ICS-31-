#Namedtuples
#step 1: set it up (say this once at the top of the program:
from collections import namedtuple
#Step 2: define what your object looks like
#a student has a name, ID, major, GPA
Student = namedtuple("Student", "name ID major GPA") #blueprint
#step 3: Create a couple of objects of this new type
student_1 = Student("Peter Anteater", "1111111", "ICS", 5.0)
#step 4: Refer to FIELDS as needed with dot notation:
#print("My GPA:", s1.GPA)
'''Why does Student start with an uppercase letter and s1 start with lowercase letter?'''
student_2 = Student ("Grace Hopper", "0000000", "CS", 5.1)
student_3 = Student("Bill Gates", "9999999", "HR", 3.0)
student_list = [student_2, student_1, student_3]
#print(student_list)
#print()
sorted_list_1 = sorted (student_list)
#print (sorted_list_1)
#print()
def student_id (apprentice: Student) -> int:
    '''Return ID number of a student'''
    return apprentice.ID
assert student_id (student_2) == '0000000'

sorted_list_2 = sorted (student_list, key = student_id)
print(sorted_list_2)


## Flow of information
##sequential
##calling a function
##Selection: choose what to do based on an answer to yes or no question
## IF statement
## repetition: loops
##  FOR loops and WHILE loops
## today --- FOR loops

##temperature = 80
##print("Here is what to wear today")
##if temperature < 55:
##    print ("Put on a jacket")
##print ("Be well")


## The IF statement
## SYNTAX (first version)
## if BOOLEAN-EXPRESSION:
##    STATEMENT(S)

##SEMANTICS:
## Evaluate the boolean expression (True or False)
## If it's true do the indented statements (the body)
## if false skip the body
## in either case to the next unindented statement


print()
temperature = 80
print("Here is what to wear today")
if temperature < 55:
    print ("Put on a jacket")
else:
    print("Wear a tshirt")
print ("Be well")

## The IF statement
## SYNTAX (first version)
## if BOOLEAN-EXPRESSION:
##    STATEMENT(S)
##else:
##    STATEMENT(S)

##SEMANTICS:
## Evaluate the boolean expression (True or False)
## If it's true do the indented statements (the body)
## if false do what's indented after else:
## in either case to the next unindented statement

temperatures = [85, 20, 42, 100, -40]

print()
print("Last week's high temperatures")
print(temperatures)
print()
for i in temperatures:
    print(i)
print("cool, isn't it?")
for t in temperatures:
    if t  > 80:
        print("The best weather ever")
    else:
        print("I am freezing")

print()
for c in "Welcome to Russia":
	print ("Next character is " + c + ".")

Book = namedtuple("Book", "title author price")
book_1 = Book ("The Sorcerer Stone", "J.K. Rowling", 66)
book_2 = Book("Cat in the Hat", "Dr. Seuss", 19)
book_3 = Book ("The Code", "Unknown", 101)

book_list = [book_3, book_2, book_1]

for b in book_list:
    print("This book is by", b.author, "and its title is", b.title)
    if b.author == "Unknown":
        print ("I don't know this author")
