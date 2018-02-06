#Franchesca Leung 78831208 and . ICS 31 Lab sec 3. Lab assignment 5.

from collections import namedtuple
Dish = namedtuple ("Dish", "name price calories")
#Part C
print("----Part C----")
print()

#c1
print("c1")
dish1 = ('Noodles', 5.00, 400)
dish2 = ('Chicken', 12.00, 600)
dish3 = ('Pancakes', 8.00, 300)

#c2
print("c2")
def dish_str(a: Dish) -> str:
    '''return string of name, price, and calories'''
    return a[0] + ' ($' + str(a[1]) + '): '+ str(a[2]) + ' cal'

assert(dish_str(dish1)) == "Noodles ($5.0): 400 cal"
print(dish_str(dish2))

#c3
print()
print("c3")
def dish_same(a: Dish, b: Dish) -> bool:
    if a[0]== b[0]:
        if a[2] == b[2]:
            return True
        else: return False
    else:
        return False

dish4 = ('Pancakes', 9.00, 300)
dish5 = ('Chicken', 12.00, 800)
assert(dish_same(dish1, dish2)) == False
assert(dish_same(dish3, dish4)) == True
assert(dish_same(dish5, dish2)) == False
print(dish_same(dish2, dish3))
