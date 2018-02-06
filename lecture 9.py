'''Lecture 9 ICS 31 Winter 2018
Problem for Piazza

Basic: Ask the user for name. If the name is Martin or Martha,
print "Have a safe trip to Lapland", otherwise print
"Nice to meet you" and user's name.

If you have time: Do it in a while loop
until user enters "exit", "quit", or "bye"

'''
##user_name = input("What is your name?")
##
##if user_name == "Martin" or user_name == "Martha":
##        print("Have a safe trip to Lapland")
##else:
##        print("Nice to meet you", user_name)
##
##user_name = input("What is your name?")
##        
##while True:
##    if user_name == "Martin" or user_name == "Martha":
##        print("Have a safe trip to Lapland")
##        user_name = input("What is your name?")
##    elif user_name == "exit" or user_name == "quit" or user_name == "bye":
##        break
##    else:
##        print("Nice to meet you", user_name)
##        user_name = input("What is your name?")
##     

#developing a restaurants program
'''one way to organize: the object -oriented:
We have Restaurants, a collection of Restaurants
Restaurants with user input, and printed
Collections created, printed, searched, added to, ...
This refers what we inside the program
we'll call this a model
the user interface, called the VIEW
'''

def restaurants() -> None:
    """Main program, starts and finishes all"""
    print("welcome to the restaurants program")
    print()
    our_diners = [] #this is our collection of restaurants
    our_diners = handle_commands (our_diners)
    #for now we are just going to throw that list away when the buser quits
    print()
    print("Thank you. Good bye")
    return

#all caps means constant
MENU  = """ 
Restaurant collection program
Choose one action
a: Add a new restaurant to collection
r: Remove a restaurant from collection
s: search the collection
p: print all the restaurants
q: quit or exit

"""

def handle_commands(diner_list: "list of Restaurant") -> "list of Restaurant":
    still_working = True
    while still_working:
            command = input(MENU)
            if command == "q":
                still_working = False
            elif command == "a":
                print("You want to add a restaurant")
            elif command == "r":
                print("You want to remover a restaurant")
            elif command == "s":
                print("You want to search restaurants")
            elif command == "p":
                 print("You want to print restaurants")
            else:
                print("You entered illegal action", command)
    return diner_list
restaurants()
##################
    
