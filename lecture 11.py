'''Lecture 9 ICS 31 Winter 2018
Problem for Piazza

Basic: Ask the user for name. If the name is Martin or Martha,
print "Have a safe trip to Lapland", otherwise print
"Nice to meet you" and user's name.

If you have time: Do it in a while loop
until user enters "exit", "quit", or "bye"

'''
#Developing a restaurants program
'''
One way to organize: the object- oriented:
We have Restaurants, a Collection of Restaurants
Restaurants with user input, and printed
Collections created, printed, searched, added to, ...
THis refers what we inside the program
We'll call this a MODEL
The user interface is the other part, called the VIEW
We'll could start with either.
The view let's us see stuff working from the beginning.
It's instant gratification, so we'll start here

'''

from collections import namedtuple # it's customary to do this at the top

#VIEW (USER INTERFACE) PORTION OF THE PROGRAM

def restaurants() -> None:
    """Main program, starts and finishes up"""
    print ("Welcome to the restaurants program")
    print()
    our_diners = [ ] # This our collection of restaurants
    our_diners = handle_commands (our_diners) # do everything
    ## For now we are just going to throw that list away 
    ## when the user quits. Later we'll write it out
    ## to a file so that we can start next time
    ## where we left offf
    
    print()
    print ("Thank you. Good bye")
    return

MENU = """
Restaurant collection program
Choose one action
a: Add a new restaurant to collection
r: Remove a restaurant to collection
s: Search the collection
p: print all the restaurants
q: quit or exit

"""

def handle_commands (diner_list: "list of Restaurant" ) -> "list of Restaurant":
    ''' Print menu, accept and handle commands to maintain list'''
    
    still_working = True
    while still_working:
        command = input(MENU)
        if command == "q":
            still_working = False # we are done, next time we'll get out of while loop 
        elif command == "a":
            print ("You want to add a restaurant")
            eatery = diner_get_info() #implemented in a model
            #diner_list = collection_add (diner_list, eatery)
        elif command == "r":
            print ("You want to remove a restaurant")
            name  = input ("Please enter the name of the restaurant" +
                           " to remove ")
            #diner_list = collection_remove_by_name (diner_list, name)
        elif command == "p":
            print ("You want to print restaurants")
            #print (collection_to_str (diner_list))
        elif command == "s":
            print ("You want to search for a restaurant")
            name = input ("Please enter the name of the restaurant" +
                           " to search for ")
            '''print (collection_to_str (collection_search_by_name (
                diner_list, name)))'''
        else:
            print ("You entered illegal action " + command, +
                   ". Please, try again.")
    return diner_list
        
## MODEL PORTION OF RESTAURANTS PROGRAM

## RESTAURANT

Restaurant = namedtuple ("Restaurant", "name cuisine phone dish price")

# Create a few restaurants for testing
diner1 = Restaurant ("Taileven", "French", "01-22-33-44-55",
                     "Escargots", 45.55)
diner2 = Restaurant ("Thai Dishes", "Thai", "334-4433", "Mee Krob", 8.95)
diner3 = Restaurant ("Thai Touch",  "Thai", "444-8888", "Larb Gai", 11.00)

print (diner1)

## Functions to implement
def restaurant_print (eatery: Restaurant) -> None: # just prints
    '''print restaurant in a readable form'''
    print ("Name:", eatery.name)
    print("Cuisine:", eatery.cuisine)
    print("Phone:", eatery.phone)
    print("Dish:", eatery.dish)
    print("Price: $", eatery.price, sep = "")
    return

restaurant_print(diner1)

def diner_to_str (diner: Restaurant) -> str:
    '''Return the restaurant in a readable form'''
    return "Name: " + diner.name + "\n" \
           "Cuisine: " + diner.cuisine + "\n"\
           "Phone: " + diner.phone + "\n" \
           "Dish: " + diner.dish + "\n" \
           "Price: " + str(diner.price) + "\n\n"

diner_to_str(diner2)

def collection_new() -> "List of Restaurants":
    ''''''
    return [ ]

def collection_add (diner_list: "List of Restaurants", diner: Restaurant) -> "List of Restaurants":
    '''return the list with a restaurant added to it'''
    diner_list.append(diner)
    return diner_list
assert collection_add(collection_new(), diner1) == [diner1]
assert collection_add([diner1, diner3], diner2) == [diner1, diner3, diner2]

def collection_to_str(diner_list: "List of Restaurants") -> str:
    '''Return a string representing the whole collection'''
    result = ""
    for r in diner_list:
        result = result + diner_to_str(r)
    return result

collection_to_str([diner1, diner3])


def diner_get_info() -> Restaurant:
    '''Get information from the user and create a diner'''
    name = input("Please input diner name")
    cuisine = input("Please enter kind of food")
    phone = input("Please enter the phone number")

    price = str(input(
#continued next week

## start everything up

restaurants()
##################
    
u
