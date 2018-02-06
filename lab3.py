# Garrett Mills 71811211 and Franchesca Leung 78831208. ICS 31 Lab sec 3. Lab Assignment 3.


#part c
print('----part c----')
#c.1
print('c1')
def abbreviate(month: str) -> str:
    '''returns the first three letter abbreviation'''
    return month[:3]
assert abbreviate('January') == 'Jan'
assert abbreviate('abril') == 'abr' 
assert abbreviate('February') == 'Feb'
assert abbreviate('March') == 'Mar'
print(abbreviate('February'))
print(abbreviate('January'))


#c.2
print()
print('c2')

def find_area_square(length: int) -> int:
    '''returns area of square'''
    return length * length
assert find_area_square(1) == 1
assert find_area_square(5) == 25
assert find_area_square(9) == 81
assert find_area_square(2) == 4

print(find_area_square(10))
print(find_area_square(2))

#c.3
print()
print('c3')
def find_area_circle(radius:int) -> int:
    '''returns the area of a circle'''
    return 3.14159 * (radius ** 2)
assert find_area_circle(1) == 3.14159
assert find_area_circle(5) == 78.53975
assert find_area_circle(0) == 0
print(find_area_circle(3))

#c.4
print()
print('c4')

def print_even_numbers(number_list: list) -> list:
    '''returns even number in list'''
    for n in number_list:
        if n%2 == 0:
            print(n)

print_even_numbers([2, 47, 31, 99, 20, 19, 23, 105, 710, 1004])
print()
print_even_numbers([1, 2, 3, 4, 5, 6])

#c.5
print()
print('c5')
def calculate_shipping(weight: float) -> float:
    if weight < 2.00:
        price = 2.00
    if weight < 10.00 and weight > 2:
        price = 5.00
    if weight > 10.00:
        price = 5.00 + ((weight - 10.00) * 1.50)
    return(price)

assert calculate_shipping(1.5) == 2.00
assert calculate_shipping(7) == 5.00
assert calculate_shipping(15) == 12.50

print(calculate_shipping(11))
print(calculate_shipping(1.9))
print(calculate_shipping(5))

###c.6
print()
print('c6 on tikinter')
import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=750, height=750)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window
def create_square(x_start, y_start, length):
    my_canvas.create_rectangle(x_start, y_start, (x_start + length), (y_start + length))

create_square(100, 100, 100)
create_square(50, 50, 100)
create_square(300, 50, 200)

#c.7
print()
print('c7 on tkinter')

def create_circle(x_start2, y_start2, diameter): 
    my_canvas.create_oval(x_start2, y_start2, (x_start2 + diameter), (y_start2 + diameter))

create_circle(200, 100, 100)
create_circle(50, 50, 100)
create_circle(300, 50, 200)


#part d
print()
print('------ part d ------')

#d.1
print()
print('d1')


from collections import namedtuple     # If this line is in your file already, you don't need it again
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

def restaurant_price(restaurant:list) -> float:
    '''returns price of restaurant'''
    return restaurant.price

assert restaurant_price(RC[0]) == 12.50
assert restaurant_price(RC[2]) == 25.50
print("$",restaurant_price(RC[1]))
print("$",restaurant_price(RC[2]))
print("$",restaurant_price(RC[5]))


#d.2
print()
print('d2')

def restaurant_list(l:list) -> list:
    restaurant_lis = sorted(l, key = restaurant_price)
    return restaurant_lis
print(restaurant_list(RC))

#d.3 & d.4
print()
print('d3 & d4')
def restaurant_price(restaurant: Restaurant) -> int:
    '''returns pice of restaurant'''
    return restaurant.price


def costliest(a_list: list) -> str:
    '''return the lists of sorted and unsorted restaurants and name of costliest restaurant'''
    print('unsorted list')
    print(a_list)
    print()
    a_list= sorted(a_list, key = restaurant_price)
    print('sorted list')
    print(a_list)
    print()
    return a_list[-1].name

#print(costliest(RC))

Rest =[
      Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 26.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)]
print("List:Rest")
print(costliest(Rest))



def costliest2(a_list: list) -> str:
    '''return the name of costliest restaurant'''
    
    a_list= sorted(a_list, key = restaurant_price)
    return a_list[-1].name
print()

print("costliest restaurant in RC:",costliest2(RC))


#part e
print()
print('------part e------')

Book = namedtuple('Book', 'author title genre year price instock')
book_store_inventory = [
    
    Book('R.K Rowling', 'Harry Potter', 'fiction', 2000, 12.99, 10),
    Book('Arthur Conan Doyle','Adventures of Sherlock Holmes', 'mystery', 1892, 21.50, 12),
    Book('Arthur Conan Doyle','Memoirs of Sherlock Holmes', 'mystery', 1894, 23.50, 14),
    Book('A.J Finn', 'The Woman in the Window', 'fiction', 2018, 22.00, 20),
    Book('J.R. Ward', 'Blood Fury', 'fiction', 2018, 10.00, 14),
    Book('Dan Brown', 'Origin', 'Technology', 2018, 13.99, 8)
    ]

#e.1
print()
print('e1')
for b in book_store_inventory:
    print(b.title)

#e.2
print()
print('e2')
def title_order(books:list) -> str:
    '''returns name of book in order'''
    return books.title
new_book_list = sorted(book_store_inventory, key = title_order)
for bb in new_book_list:
    print(bb.title)

#e.3
print()
print('e3')
def price_change(b_list:list) -> float:
    '''increase price by 10%'''
    for p in range(len(b_list)):
        b_list[p] = b_list[p]._replace(price = b_list[p].price*1.1)

price_change(book_store_inventory)
for bbb in book_store_inventory:
    print(bbb.title, 'is $', round(bbb.price,2))

#e.4
print()
print('e4')
for bbbb in book_store_inventory:
    if bbbb.genre == 'Technology':
        print (bbbb.title)

#e.5
print()
print('e5')
books_before_2000 = []
books_after_2000 = []
def year_published(c_list: list) -> list:
    '''add book to list by year'''
    for bbbbb in c_list:
        if bbbbb.year < 2000:
            books_before_2000.append(bbbbb.title)
        else:
           books_after_2000.append(bbbbb.title)
    print("Books published on or after 2000:", books_after_2000)
    print("Books published before 2000:", books_before_2000)

year_published(book_store_inventory)

if (len(books_before_2000)) > (len(books_after_2000)):
    print("More titles before 2000 (", (len(books_before_2000)), "vs.", (len(books_after_2000)), ")")
else:
    print("More titles 2000 or after (", (len(books_after_2000)), "vs.", (len(books_before_2000)), ")")


#e.6
print()
print('e6')
def inventory_value(Book1: object) -> int:
    '''returns value of our inventory of a book'''
    value = Book1.price * Book1.instock
    return value


def top_value(book2: list) -> object:
    values=[]
    values = sorted(book2, key = inventory_value)
    return values[-1]
    

print("The highest-inventory-value book is:", top_value(book_store_inventory).title, "by", top_value(book_store_inventory).author, "at a value of $", (round(inventory_value(top_value(book_store_inventory)),2))) 



#f
print()
print()
print('------part f------')
print('on tkinter')
def draw_eye(x_start2, y_start2, x_end2, y_end2, color):
    my_canvas.create_oval(x_start2, y_start2, x_end2, y_end2, fill=color)
    my_canvas.create_oval(x_start2 + 50, y_start2+50, x_end2-10, y_end2-10, fill='black')


def draw_nose(x1, y1, x2, y2, color):
    my_canvas.create_line(x1, y1, x2, y2, fill=color)
    my_canvas.create_line(x1, y1, x2, y2, fill=color)
    my_canvas.create_line(x1, y1, x2, y2, fill=color)


def draw_mouth(x4, y4, x5, y5):
       my_canvas.create_oval(x4, y4, x5, y5, fill='red')


def draw_face(m):
    if m > 1:
        my_canvas.create_oval(5*m, 5*m, 175*m, 175*m)
        draw_eye(25*m, 25*m, 75*m, 75*m, 'brown')
        draw_eye(100*m, 25*m, 150*m, 75 * m, 'brown')
        draw_nose(75*m, 100*m, 100*m, 100*m, 'brown')
        draw_nose(87.5*m, 75*m, 100*m, 100*m, 'brown')
        draw_nose(87.5*m, 75*m, 75*m, 100*m, 'brown')
        draw_mouth(75*m, 125*m, 100*m, 150*m)
        
draw_face(2)
draw_face(4)
draw_face(3)


tkinter.mainloop()

