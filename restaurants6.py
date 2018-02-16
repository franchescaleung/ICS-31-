#RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, Winter 2018

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)
from collections import namedtuple
Dish = namedtuple ("Dish", "name price calories") #using to test
#d1 = Dish('noodles', 4.00)
def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")
    return
MENU = """
Restaurant Collection Program --- Choose one
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 q:  Quit
 e:  Remove (erase) all the restaurants from the collection
 c:  Change prices for the dishes served
 m:  Search for specific cuisine
 w:  Search for specific word or phrase
"""

def dish_change_price(d: "list of dishes", b: float) -> "list of dishes":
    dishlist = []
    for i in d:
        i = i._replace(price = i.price * (1 + (b/100)))
        dishlist.append(i)
    return dishlist

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
            diners = collection_change_prices(diners, percent)
        elif response == 'm':
            c = input("Please enter cuisine: ")
            d = collection_search_by_cuisine(diners, c)
            for rest in d:
                print(restaurant_str(rest))
        elif response == 'w':
            g = input("Please enter a word or phrase: ")
            e = collection_search_by_word(diners, g)
            print(diners)
            for item in e:
                print(restaurant_str(item))           
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:     " + menu_display(self.menu) + "\n" +
        "Average Price:    $" + str(avg_price(self.menu)) + "\n" +
        "Average Calories: " + str(avg_calories(self.menu)) + "\n\n") 

def restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    a = input("Please enter the restaurant's name:  ")
    b = input("Please enter the kind of food served:  ")
    c = input("Please enter the phone number:  ")
    return Restaurant(a, b, c, menu_enter())

def restaurant_change_price(a: Restaurant, b: float) -> "list of restaurants":
    '''change restaurant price'''
    new = []
    for i in range(len(a.menu)):
        new.append(dish_change_price(a.menu[i], b))
    return new


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
    return s;


    

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
    newprices = []
    for i in diners:
        i = i._replace(price = i.price * (1 + (n/100)))
        newprices.append(i)
    return newprices

def collection_search_by_cuisine(m: list, cuisine: str) -> list:
    '''returns list of restaurant that matches cuisine'''
    match = []
    for rest in m:
        if rest.cuisine == cuisine:
            match.append(rest)
    return match
def collection_search_by_word(m: list, word: str) -> list:
    woo = []
    for rest in m:
        for i in rest.menu:
            if word in i.name:
                woo.append(rest)
    return woo


###DISHES

def dish_str(a: Dish) -> str:
    '''return string of name, price, and calories'''
    return a.name + ' ($' + str(a.price) + '): '+ str(a.calories) + ' cal'


def dish_get_info() -> Dish:
    """ Prompt user for fields of Dish; create and return.
    """
    return Dish(
        input("Please enter the dish's name:  "),
        float(input("Please enter the price of the dish:  ")),
        int(input("Please enter the amount of calories:")))



###MENUS

def menu_enter() -> Dish:
    '''asks user if he or she wants to make new dish'''
    menu = []
    working = True
    while True:
        user = input("Do you want to create a dish?")
        if user == 'yes':
            new_dish = dish_get_info()
            menu.append(new_dish)
        elif user == 'no':
            return menu


            
def avg_price(m: list) -> float:
    '''returns avg price of dishes in menu'''
    p = []
    for i in m:
        p.append(i.price)
    return sum(p)/len(p)

def avg_calories(m:list) -> int:
    p = []
    for i in m:
        p.append(i.calories)
    return sum(p)/len(p)
    
def menu_display(diners: list) -> str:
    '''returns menu'''
    m = ""
    for i in diners:
        m += dish_str(i) + "\n"
    return m



restaurants()




