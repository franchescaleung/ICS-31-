'''Lecture 13 ICS 31 Winter 2018

#Developing a restaurants program

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
    choice = '''If you'd like to read diners from existing file,
type the name of this file, otherwise hit return
'''
    filename = input(choice)
    if filename != "":
        our_diners = fill_in_collection_from_file(filename)
        # This is our existing collection of restaurants
    else:
        our_diners = collection_new()# start with empty collection
         
    our_diners = handle_commands (our_diners) # do everything
    

    write_file_from_collection (our_diners)
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
            still_working = False # we are done,
            #`  next time we'll get out of while loop 
        elif command == "a":
            #print ("You want to add a restaurant")
            eatery = diner_get_info() #implemented in a model
            diner_list = collection_add (diner_list, eatery)
        elif command == "r":
            #print ("You want to remove a restaurant")
            name  = input ("Please enter the name of the restaurant" +
                           " to remove ")
            diner_list = collection_remove_by_name (diner_list, name)
        elif command == "p":
            #print ("You want to print restaurants")
            print (collection_to_str (diner_list))
        elif command == "s":
            #print ("You want to search for a restaurant")
            name = input ("Please enter the name of the restaurant" +
                           " to search for ")
            print (collection_to_str (collection_search_by_name (
                diner_list, name)))
        else:
            print ("You entered illegal action " + command, +
                   ". Please, try again.")
    return diner_list
        
## MODEL PORTION OF RESTAURANTS PROGRAM

## RESTAURANT

Restaurant = namedtuple ("Restaurant", "name cuisine phone dish price")

# Create a few restaurants for testing
diner1 = Restaurant ("Tailevent", "French", "01-22-33-44-55",
                     "Escargots", 45.55)
diner2 = Restaurant ("Thai Dishes", "Thai", "334-4433", "Mee Krob", 8.95)
diner3 = Restaurant ("Thai Touch",  "Thai", "444-8888", "Larb Gai", 11.00)

print (diner1)

## Functions to implement
def restaurant_print (eatery: Restaurant) -> None: # just prints
    '''Print restaurant in a readable form'''
    print ("Name:", eatery.name)
    print ("Cuisine:", eatery.cuisine)
    print ("Phone:", eatery.phone)
    print ("Dish:", eatery.dish)
    print ("Price $", eatery.price, sep = "")
    return
restaurant_print(diner1)
## Using \ to tell Python the statement
## is continued on the next line
def diner_to_str (diner:Restaurant) -> str:
    '''Return the restaurant in a readable form'''
    return "Name: " + diner.name + "\n" \
           "Cuisine: " + diner.cuisine + "\n" \
           "Phone: " + diner.phone + "\n" \
           "Dish: " + diner.dish + "\n" \
           "Price: $" + str(diner.price) + "\n\n"
diner_to_str (diner1)

## Using parens as an alternative to backslash
def diner_to_str (diner:Restaurant) -> str:
    '''Return the restaurant in a readable form'''
    return ("Name: " + diner.name + "\n" 
           "Cuisine: " + diner.cuisine + "\n" 
           "Phone: " + diner.phone + "\n" 
           "Dish: " + diner.dish + "\n" 
           "Price: $" + str(diner.price) + "\n\n")
#print (diner_to_str (diner2))

def diner_to_tabbed_string(r: Restaurant) -> str:
    ''' Return a string containing the restaurant's fields,
        separated by tabs [for writing to a file]
    '''
    pass

## COLLECTION
# A collection of Restaurants is a list of Restaurant objects
# But some day we might choose a different form, a different way
# to represent collections (e.g., a dictionary).  If we give the
# rest of our development team our API (Aplication Programming
# Interface), the names of functions, the types of their arguments,
# and what the function DOES), that should be enough for them.
# They shouldn't have to know the internals of our code.

test_diners = [diner1, diner2, diner3]   # "Test Restaurant Collection

def collection_new () -> "List of Restaurant":
    '''Creating new collection'''
    return [ ]

def collection_add (diner_list: "List of Restaurant",
                    diner: Restaurant) -> "List of Restaurant":
    '''Return the list with a restaurant added to it'''
    diner_list.append (diner)
    return diner_list

assert collection_add (collection_new(), diner1) == [diner1]
assert collection_add ([diner1, diner3], diner2) == [diner1, diner3, diner2]

## It's a simple function because main work is done in
## diner_to_str and now we can just call it
def collection_to_str (diner_list: "List of Reastaurant") -> str:
    '''Return a string representing the whole collection'''
    result = ""
    for r in diner_list:
        result = result + diner_to_str (r)
    return result

print (collection_to_str ([diner1, diner3]))
assert collection_to_str (collection_new()) == ""
assert collection_to_str (test_diners) == diner_to_str (diner1) +\
       diner_to_str (diner2) + diner_to_str (diner3)

def diner_get_info () -> Restaurant:
        
    '''Get information from the user and create a diner'''
    name = input("Please input diner name: ")
    cuisine = input ("Please enter kind of food served: ")
    phone = input ("Please enter the phone number: ")
    dish = input("Please enter the name of the best dish:  ")
    price = input("Please enter the price of that dish:  ")
    return Restaurant(name, cuisine, phone, dish, float(price))
    
#diner4 = diner_get_info()
#print (diner4)
#print (diner_to_str(diner4))

def collection_search_by_name (diner_list:"list of Restaurant",
                               looking_for:str) -> "list of Restaurant":
    '''Return restaurants matching looking_for'''
    result = []
    for d in diner_list:
        if d.name == looking_for:
            result.append(d)
    return result
#find existing restaurant
assert collection_search_by_name (test_diners, "Tailevent") == [diner1]
#find restaurant not on the list
assert collection_search_by_name (test_diners, "Wok") == [ ]
#find multiple occurences (e.g. a list of award winners by the year)
assert collection_search_by_name([diner2, diner1, diner2, diner3], "Thai Dishes") == \
       [diner2, diner2]

def collection_remove_by_name (diner_list:"list of Restaurant",
                               to_remove:str)-> "list of Restaurant":
    '''Return diners with matching diner removed'''
    result = [ ]
    for d in diner_list:
        if d.name != to_remove:
            result.append(d)
    return result

### Test cases:  Many configurations
# Remove from the empty list [still empty]
assert collection_remove_by_name ([ ], "Tailevent") == [ ]
# Remove item from list, result empty
assert collection_remove_by_name ([diner1], "Tailevent") == [ ]
# Remove item not on list at all
assert collection_remove_by_name (test_diners, "Wendy") == test_diners
assert collection_remove_by_name ([diner1,diner2], "Tailevent") == [diner2]
# Remove first item from list
assert collection_remove_by_name (test_diners, "Tailevent") == [diner2, diner3]
# Remove last item on list
assert collection_remove_by_name (test_diners, "Thai Touch") == [diner1, diner2]
# Remove from middle of list
assert collection_remove_by_name (test_diners, "Thai Dishes") == [diner1, diner3]
# Remove multiple occurrences of name
assert collection_remove_by_name([diner3, diner2, diner3, diner1, diner3],
                                 "Thai Touch") == [diner2, diner1]
'''Need to write 2 functions:'''


 def diner_to_tabbed_string(r: Restaurant) -> str:
     '''return tabbed string'''
     return r.name + "\t" + r.cuisine + "\t" +\
            r.phone + "\t" + r.dish + "\t" + \
            str(r.price)
def fill_in_collection_from_file(filename: str) -> 'list of Restaurant':
    ''' Read restaurant info from (tab-delimited) file, return
        collection.  '''
    result = []
    infile = open(filename, "r")
    for line in infile:
        field_line = line.split("\t")
        new_diner = Restaurant(field_list[0],field_list[1],field_list[2],field_list[3], float(field_list[4]))
        result.appned(new_diner)
        infile.close()
        return result

def write_file_from_collection (our_diners:'list of Restaurant') -> None:
    ''' Write file called restaurants.txt, tab-delimited
    '''
    outfile = open("diner.txt", "w")
    for diner in our_diners:
        outfile.write(diner_to_tabbed_string(diner) + "\n")
    outfile.close()
    return

## start everything up

restaurants()
##################
    



