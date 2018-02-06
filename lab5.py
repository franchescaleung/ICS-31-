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
print(len(dish_list_1))
dish_list_2 = [dish6, dish7, dish8, dish9]
dish_list_1.extend(dish_list_2)
print(dish_list_1)

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
    for i in a:
        if b > 100:
            a = a._replace(price = i.price * (b/100))
        if b < 100:
            a = a._replace(price = i.price * (1 + (b/100)))
        if b == 100:
            a = a._replace(price = i.price * 1)

print(dishlist_change_price(dish_list_1, 120))
        
