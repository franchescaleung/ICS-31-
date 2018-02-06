#Harmandeep Bagri 12856273 and Franchesca Leung 78831208. ICS 31 sec 3. Lab Assignment 4.

#c
print("-----Part C-----")
print()
#c1
print("c1")
def test_number(number:int, s:str):
    '''returns whether number is even, odd, positive, or negative'''
    if s == 'even':
        if number % 2 == 0:
            return True
        else:
            return False
    elif s == 'odd':
        if number % 2 != 0:
            return True
        else:
            return False
    elif s == 'positive':
        if number >= 0:
            return True
        else:
            return False
    elif s == "negative":
        if number < 0:
            return True
        else:
            return False
        
assert test_number(14, 'even') == True
assert not test_number(100, 'odd') == True
assert test_number(33, 'positive') == True
assert not test_number(100, 'negative') == True

print(test_number(5, 'even'))
print(test_number(7, 'odd'))
print(test_number(-9, 'negative'))
print(test_number(1, 'positive'))

#c2
print()
print('c2')
def display():
    '''takes in a word and prints one letter on each line'''
    word = input("Enter a word:")
    for l in word:
        print(l)
    return

display()

#c3
print()
print('c3')
def cube_list(list_of_ints: list) -> 'ints cubed':
    '''returns the cubed number of each number in list'''
    for i in list_of_ints:
        cubed = i ** 3
        print (cubed)
    return
cube_list([2, 3, 4, 10])

#c4
print()
print('c4')
def match_first_letter(s: str, li: list):
    '''prints out words that start with the one-character'''
    for w in li:
        if w[0] == s:
            print(w)
    return
    

match_first_letter('I', ['Iron Man', 'Iron Lady', 'The Avengers', 'Superman', 'I am Legend'])
    
#c5
print()
print("c5")
def match_area_code(area_codes: list, phone_numbers:list):
    '''returns matching numbers'''
    matched = []
    for code in area_codes:
        for num in phone_numbers:
            if code == num[1:4]:
                matched.append(num)
    for item in matched:
        print(item)
    return
                    
match_area_code(['949', '714'], ['(714)948-1234', '(419)949-8732', '(949)555-1234'])

#c6
print()
print('c6')

def matching_area_codes(area_codes: list, phone_numbers:list):
    'returns list of matching numbers'''
    matched = []
    for code in area_codes:
        for num in phone_numbers:
            if code == num[1:4]:
                matched.append(num)
    return (matched)

print(matching_area_codes(['949', '714'], ['(714)948-1234', '(419)949-8732', '(949)555-1234']))

#part d
print()
print("-----Part D-----")
print()
#d1
print("d1")
def is_vowel(s: str) -> bool:
    '''returns True if letter s is in a vowel'''
    vowels = ["a", "A", 'e', 'E', 'i','I' ,'o', "O", 'u', "U"]
    return (s in vowels)

assert(is_vowel("e")) == True
assert(is_vowel("v")) == False
       
print(is_vowel("E"))
print(is_vowel("s"))

#d2
print()
print("d2")
def print_nonvowels(s:str):
    ''' prints out all the non vowel car in the string'''
    for i in s:
        if not is_vowel(s):
            print(i)
    return


    
print_nonvowels("iukhj")
print_nonvowels("dog")

#d3
print()
print("d3")
def nonvowels(s:str) -> str:
    '''takes string and returns a string containing all characters that are not vowels'''
    result = ""
    for w in s:
        if (is_vowel(w)) == False:
            result+=w
    return result

assert nonvowels('apple') == 'ppl'
assert nonvowels('hey') == 'hy'
print(nonvowels("hey"))
print(nonvowels('happy birthday!'))


assert is_vowel('a') 
assert is_vowel('U')
assert not is_vowel('X')
assert not is_vowel('?')


def double(x:float) -> float:
     return(x * 2)

assert double(0) == 0
assert double(17.5) == 35
assert double(-223344) == -446688     
print(double(2))

#d4
print()
print("d4")
def consonants(s:str) ->str:
    '''takes a string and returns a string containing the non vowel letters'''
    con = ['b', 'B', 'c', 'C', 'd','D','f', 'F', 'g','G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'v', 'V', 'w', 'W','x', 'X', 'y','Y', 'z', 'Z']
    empty=""
    for i in s:
        if i in con:
            empty +=i
    return empty
assert(consonants("hi")) == "h"
assert(consonants("happy birthday")) == "hppybrthdy"
print(consonants("hey you"))

#d5
print()
print("d5")
def select_letters(a:str, b:str) -> str:
    '''takes two parameters and returns vowels if first variable is v and returns consonants if first variable is c'''
    letters = ""
    if a == 'v':
        for i in b:
            if (is_vowel(i) == True):
                letters +=i
    elif a == 'c':
        for w in b:
            if (is_vowel(w) == False):
                letters += w
    return letters

assert(select_letters('v', 'facetiously')) == 'aeiou'
assert(select_letters('c', 'facetiously')) == 'fctsly'

print(select_letters('c', 'happy'))

#d6
print()
print("d6")
print()

def hide_vowels(a:str) -> str:
    '''replaces vowels in given string with -'''
    r = ""
    for i in a:
        if (is_vowel(i) == True):
            r += "-"
        else:
            r += i
    return r

assert(hide_vowels("what")) == 'wh-t'
assert(hide_vowels("computer science")) == 'c-mp-t-r sc--nc-'
print(hide_vowels("hey there buddy"))

#e
from collections import namedtuple

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number,
#       best dish, price of that dish

restaurant_1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
restaurant_2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
restaurant_3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
restaurant_4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
restaurant_5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
restaurant_6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
restaurant_7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
restaurant_8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
restaurant_9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
restaurant_10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
restaurant_11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
restaurant_12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
restaurant_13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
restaurant_14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
restaurant_15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
restaurant_16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
restaurant_17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
restaurant_18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
restaurant_19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
restaurant_20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
restaurant_21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
restaurant_22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
restaurant_23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
restaurant_24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
restaurant_25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
restaurant_26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


restaurant_list = [restaurant_1, restaurant_2, restaurant_3, restaurant_4, restaurant_5, restaurant_6, restaurant_7, restaurant_8, restaurant_9, restaurant_10, restaurant_11, restaurant_12, restaurant_13, restaurant_14, restaurant_15, restaurant_16, restaurant_17, restaurant_18, restaurant_19, restaurant_20, restaurant_21, restaurant_22, restaurant_23, restaurant_24, restaurant_25, restaurant_26]
print()
print("-----Part E-----")
print()
def restaurant_change_price(r: Restaurant, n: int) -> Restaurant:
    '''changes price of restaurant and returns the new price along with the same contents of the restaurant'''
    r = r._replace(price = r.price * n)
    return r

print(restaurant_change_price(restaurant_2, 4)) 
print(restaurant_change_price(restaurant_1, 2))

#f
print()
print('-----Part F-----')
print()
#f1
print("f1")

def alphabetical(r: "list of Restaurants") -> "list of Restaurants":
    '''returns list in alphabetical order'''
    return sorted(r)

print(alphabetical(restaurant_list))
    
#f2
print()
print("f2")
print()

def alphabetical_names(r: "list of Restaurants") -> "list of Restaurant names":
    '''returns restaurant names in alphabetical order in a list'''
    a = alphabetical(r)
    b = []
    for i in a:
         b.append(i[0])
    return b
    
print(alphabetical_names(restaurant_list))


#f3
print()
print("f3")
print()

def all_thai(l: "list of Restaurants") -> "list of Restaurants":
    '''takes a list of restaurants and returns all thai restaurants'''
    thai = []
    for r in l:
        if (r.cuisine == 'Thai'):
            thai.append(r)
    return thai

print(all_thai(restaurant_list))


#f4
print()
print("f4")
print()

def select_cuisine(l: "list of Restaurants", c: str) -> "list of restaurants":
    '''returns all restaurants in given cuisine'''
    cuisine_list = []
    for r in l:
        if (r.cuisine == c):
            cuisine_list.append(r)
    return cuisine_list

print(select_cuisine(restaurant_list, 'Chinese'))

#f5
print()
print("f5")
print()

def select_cheaper(l:"list of Restaurants", n: float) -> "list of restaurants":
    ''' returns list of all restaurants is less than given number'''
    rest = []
    for i in l:
        if (i.price < n):
            rest.append(i)
    return rest

print(select_cheaper(restaurant_list, 10))

#f6
print()
print("f6")
print()

def average_price(l: "list of Restaurants") -> "list of Restaurants":
    ''' returns average price of the price of the best dishes at all the restaurants in list'''
    total = 0
    
    for i in l:
        total += i.price
    average = total / (len(l))
    return average

print("average price: $", round(average_price(restaurant_list), 2))

#f7
print()
print("f7")
print()

print("Average price of Indian food: $", average_price(select_cuisine(restaurant_list, "Indian")))

#f8
print()
print("f8")
print()

print("Average price of Chinese and Thai food: $", round(average_price((select_cuisine(restaurant_list, "Thai")) + (select_cuisine(restaurant_list, "Chinese"))),2))

#f9
print()
print("f9")
print()
print(alphabetical_names(select_cheaper(restaurant_list, 15)))


#G
print()
print("---Part G---")
print()
import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

def create_rectangle_from_center(x: int, y:int, height: int, width: int):
    '''create rectangle based on center points'''
    my_canvas.create_rectangle((x - (width/2)), (y - (height/2)), ((width/2 )+x), ((height/2) +y))

create_rectangle_from_center(250, 250, 200, 200)
tkinter.mainloop()
