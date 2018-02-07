# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, Winter 2018

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 q:  Quit
 e:  Remove (erase) all the restaurants from the collection
 c:  Change prices for the dishes served
"""
def restaurant_change_price(a: "list of restaurants", b: float) -> "list of restaurants":
    '''change restaurant price'''
    for i in range(len(a)):
            a[i]= a[i]._replace(price = a[i].price * (1 + (b/100)))
    return a
def handle_commands(diners: list) -> list:
    """ Display menu, accept and process commands.
    
    """
    done = False
    while not done:
        response = input(MENU)
        if response=="q":
            done = True
            return diners
        elif response=='n':
            r = restaurant_get_info()
            diners = collection_add(diners, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            diners = collection_remove_by_name(diners, n)
        elif response=='p':
            print(collection_str(diners))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in collection_search_by_name(diners, n):
                print(restaurant_str(r))
        elif response == 'e':
            diners = []
        elif response == 'c':
            percent = float(input("How big of a change?"))
            collection_change_prices(diners, percent)
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Dish:     " + self.dish + "\n" +
        "Price:    ${:2.2f}".format(self.price) + "\n\n")

def restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        input("Please enter the name of the best dish:  "),
        float(input("Please enter the price of that dish:  ")))


#### COLLECTION
# A collection is a list of restaurants

def collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def collection_str(diner_collection: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in diner_collection:
        s = s + restaurant_str(r)
    return s

def collection_search_by_name(diner_list: list, diner_name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in diner_list:
        if r.name == diner_name:
            result.append(r)
    return result

def collection_add(diner_list: list, diner: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    diner_list.append(diner)
    return diner_list

def collection_remove_by_name(diners: list, diner_name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in diners:
        if r.name != diner_name:
            result.append(r)
    return result
def collection_change_prices(diners: list, n: float) -> list:
    '''changes price of whole collection'''
    restaurant_change_price(diners, n)
    return diners

restaurants()

