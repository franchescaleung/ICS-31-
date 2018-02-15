#Franchesca Leung 78831208 and Brianna Fong 79235846. ICS 31 Lab sec 3. Lab assignment 5.

from collections import namedtuple
Dish = namedtuple ("Dish", "name price calories")
#Part C
print("----Part C----")
print()

#c1
print("c1")
dish1 = Dish('Noodles', 5.00, 400)
dish2 = Dish('Chicken', 12.00, 600)
dish3 = Dish('Pancakes', 8.00, 300)

#c2
print("c2")
def dish_str(a: Dish) -> str:
    '''return string of name, price, and calories'''
    return a.name + ' ($' + str(a.price) + '): '+ str(a.calories) + ' cal'

assert(dish_str(dish1)) == "Noodles ($5.0): 400 cal"
print(dish_str(dish2))

#c3
print()
print("c3")
def dish_same(a: Dish, b: Dish) -> bool:
    return a.name == b.name and a.calories == b.calories

dish4 = Dish('Pancakes', 9.00, 300)
dish5 = Dish('Chicken', 12.00, 800)
assert(dish_same(dish1, dish2)) == False
assert(dish_same(dish3, dish4)) == True
assert(dish_same(dish5, dish2)) == False
print(dish_same(dish2, dish3))


#c4
print()
print("c4")

def dish_change_price(a: Dish, b: float) -> Dish:
    '''takes dish and returns a different price'''
    if b < 0:
        a = a._replace(price = (-1*(b/100)) * a.price)
    if b > 0:
        a = a._replace(price = (1 + (b/100)) * a.price)
    return a

print(dish_change_price(dish1, 100))

#c5
print()
print("c5")
def dish_is_cheap(a: Dish, b: float) -> bool:
    '''returns true if dish price is less than number otherwise false'''
    if a.price < b:
        return True
    else:
        return False
assert(dish_is_cheap(dish1, 6)) == True
assert(dish_is_cheap(dish4, 7)) == False

#c6

print()
print("c6")
dish6 = Dish('Spaghetti', 18.75, 400)
dish7 = Dish('Salad', 23.25, 100)
dish8 = Dish('Donuts', 18.90, 400)
dish9 = Dish('Steak', 22.50, 800)
dish_list_1 = [dish1, dish2, dish3, dish4, dish5]
print("length of dish list", len(dish_list_1))
print()
dish_list_2 = [dish6, dish7, dish8, dish9]
dish_list_1.extend(dish_list_2)
print("List of dish list 1", dish_list_1)

print()
def dishlist_display(a: "list of dishes") -> str:
    '''returns string of dishes'''
    empty = ""
    for i in a:
        empty += str(i) + "\n"
    return empty

print(dishlist_display(dish_list_1))

#c7
print()
print("c7")
def dishlist_all_cheap(a: "list of dishes", b: float) -> bool:
    '''returns true if the price of every dish in list is less than given number'''
    for i in a:
        if i.price > b:
            return False
    return True
assert(dishlist_all_cheap(dish_list_2, 20)) == False
print(dishlist_all_cheap(dish_list_1, 30))           

#c8
print()
print("c8")
def dishlist_change_price(a: "list of dishes", b: float) -> "list of dishes":
    ''' takes dishes and percentage change and returns a list of dishes with price change'''
    for i in range(len(a)):
            a[i] = a[i]._replace(price = a[i].price * (1 + (b/100)))
    
dishlist_change_price(dish_list_1, 120)
print(dish_list_1)
        
#c9
print()
print("c9")
def dishlist_prices(a: "list of dishes") -> "list of prices":
    '''takes list of dish and returns list of prices'''
    prices=[]
    for i in a:
        prices.append(i.price)
    return prices
print(dishlist_prices(dish_list_2))


#c10
print()
print("c10")
def dishlist_average(a: "list of dishes") -> float:
    '''takes list of dishes and returns average price of all'''
    total = 0
    for i in a:
        total += i.price
    average = total / (len(a))
    return average

dish10 = Dish('Pizza', 10.00, 500)
dish11 = Dish('Fries', 3.00, 300)
dishlist3 = [dish10, dish11]
print(dishlist_average(dishlist3))

#c11
print("c11")
def dishlist_keep_cheap(a: "list of dishes", b: float) -> "list of dishes":
    newlist = []
    for i in a:
        if i.price < b:
            newlist.append(i)
    return newlist
print(dishlist_keep_cheap(dishlist3, 5))

#c12
print("c12")
dish12 = Dish('Shrimp', 22, 312)
dish13 = Dish('Fried Rice', 36.55, 415)
dish14 = Dish('Mac n Cheese', 24.98, 222)
dish15 = Dish('Lasagna', 43, 498)
dish16 = Dish('Pizza', 34.95, 333)
dish17 = Dish('Chicken Wings', 24, 988)
dish18 = Dish('Salmon', 33.33, 789)
dish19 = Dish('Eggs', 10.99, 99)
dish20 = Dish('Omlette', 100, 666)
dish21 = Dish('Chicken Tenders', 65.50, 345)
dish22 = Dish('Dumplings', 23.99, 534)
dish23 = Dish('Clams', 78.99, 690)
dish24 = Dish('Cake', 50, 564)
dish25 = Dish('Cheesecake', 33.45, 980)
biglist = [dish1, dish2, dish3, dish4, dish5, dish6, dish7, dish8, dish9, dish10, dish11, dish12, dish13, dish14, dish15, dish16, dish17, dish18, dish19, dish20, dish21, dish22, dish23, dish24, dish25] 
def before_and_after():
    percentage_change = int(input("How big is the percentage change?"))
    print("Original prices:", dishlist_display(biglist))
    dishlist_change_price(biglist, percentage_change)
    print("New prices:", dishlist_display(biglist))

before_and_after()    

#part e
print()
print("---Part E---")
print()
#e1
print("e1")
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])
r3 = Restaurant('Pascal', 'French', '940-752-0107', [Dish('Escargots', 12.95, 250),
                                                     Dish('Poached salmon', 18.50, 550),
                                                     Dish('Rack of lamb', 24.00, 850),
                                                     Dish('Marjolaine Cake', 8.50, 950)])
r4 = Restaurant('Pascal', 'French', '940-752-0107', [])
list_of_restaurants = [r1, r2, r3]

#e2
print("e2")
print()
def restaurant_first_dish_name(a: Restaurant) -> str:
    '''returns name of first dish in restauarant'''
    name = ""
    if a.menu == []:
        return name
    else:
        return a.menu[0].name
assert(restaurant_first_dish_name(r3)) == 'Escargots'
assert(restaurant_first_dish_name(r4)) == ""
print(restaurant_first_dish_name(r2))

#e3
print()
print("e3")
print()
def restaurant_is_cheap(a: Restaurant, n: float) -> bool:
    '''returns true if the average price is less than or equal to number'''
    total = 0
    for i in a.menu:
            total += i.price
    average = total / (len(a.menu))
    if average <= n:
        return True
    else:
        return False
assert(restaurant_is_cheap(r1, 10)) == False 
print(restaurant_is_cheap(r1, 20))

#e4
print()
print("e4")
print()


def dish_raise_price(d:Dish, x: float) -> float:
    '''adds 2.50 to price of dish'''
    d = d._replace(price = d.price + x)
    return d


def menu_raise_prices(m: "list of dish", x: float) -> "menu":
    '''returns new menu prices with x amount changed'''
    new_dish_list = []
    for i in m:
        s = dish_raise_price(i, x)
        new_dish_list.append(s)
    return new_dish_list

def restaurant_raise_prices(r: Restaurant) -> float:
    newrestaurant = r._replace(menu = menu_raise_prices(r.menu, 2.50))
    return newrestaurant


def collection_raise_prices(a: "list of restaurants") -> "list of restaurants":
    new_collection = []
    for i in a:
        b = restaurant_raise_prices(i)
        new_collection.append(b)
    return new_collection

print(collection_raise_prices(list_of_restaurants))
print()

def collection_change_price(a: "list of restaurants", b: float) -> "list of restaurants":
    newcollection = []
    for i in a:
        newmenu = []
        for j in i.menu:
            if b < 0:
                j = j._replace(price = (-1*(b/100)) * j.price)
                newmenu.append(j)
            if b > 0:
                j = j._replace(price = (1 + (b/100)) * j.price)
                newmenu.append(j)
        
        i = i._replace(menu = newmenu)
        newcollection.append(i)
    return newcollection
print(collection_change_price(list_of_restaurants, 100))
   
#e5
print()
print("e5")
print()
def collection_select_cheap(a: "collection",n: float) -> "list of restaurants":
    ''' returns a list of restaurants with avergae price less than n'''
    cheap = []
    for i in a:
        if restaurant_is_cheap(i, n) == True:
            cheap.append(i)
    return cheap

print(collection_select_cheap(list_of_restaurants, 15))


#part g
print()
print("---Part G---")
print()
Count = namedtuple("Count", "letter number")
def for_one(a: str, b: str) -> int:
    x = 0
    for i in a:
        if i == b:
            x +=1
    count = Count(b, x)
    return count
print(for_one("some", "o"))

def letter_count(a: str, b: str) -> int:
    '''returns letter count'''
    newlist = []
    for j in b:
        s = for_one(a,j)
        newlist.append(s)
    return newlist

assert(letter_count('The cabbage has baggage', 'abcd')) == [Count(letter='a',number=5), Count(letter='b',number=3), Count(letter='c',number=1), Count(letter='d',number=0)]
print(letter_count('sooome', 'oe'))




