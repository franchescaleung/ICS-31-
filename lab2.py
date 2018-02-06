# Franchesca Leung 78831208 and yijun zhou 52533998. ICS 31 Lab sec 3. Lab Assignment 2.

#c
print("How many hours?")
hours = float(input())
print("This many hours:", hours)
print("How many dollars per hour?")
rate = float(input())
print("This many dollars per hour:  ", rate)
print("Weekly salary:  ", hours * rate)

#c1
hours = int(input("How many hours?"))
print("This many hours:", hours)
rate = float(input("How many dollars per hour?"))
print("This many dollars per hour: $", rate)
print("Weekly salary: $ ", hours * rate)


#c2
print ('Hello. What is your name?')
name = input()
print ('Hello,', name)
print("It's nice to meet you.")
print ("How old are you?")
age= int(input())
next_year= age+1
print ("Next year you will be", next_year,"years old.")
print("Good-bye!")

#d

KRONE_PER_EURO = 7.46
KRONE_PER_POUND = 8.60
KRONE_PER_DOLLAR = 6.62

print("Please provide this information:")
business_name = input("Business name:")
number_of_euros = (int(input("Number of euros:")))
number_of_pounds = (int(input("Number of pounds:")))
number_of_dollars = (int(input("Number of dollars:")))

print("Copenhagen Chamber of Commerce")
print("Business name:", business_name)
euros_to_krone = number_of_euros * KRONE_PER_EURO
pounds_to_krone = number_of_pounds * KRONE_PER_POUND
dollars_to_krone = number_of_dollars * KRONE_PER_DOLLAR
print(number_of_euros, "euros is", euros_to_krone, "krone")
print(number_of_pounds, "pounds is", pounds_to_krone, "krone")
print(number_of_dollars, "dollars is", dollars_to_krone, "krone")
total = euros_to_krone + pounds_to_krone + dollars_to_krone

print("Total krone:", total)

###e
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)
###e.1
print (still_another[0])
###e.2
print(another[3])
###e.3
average_price=(favorite[3]+another[3]+still_another[3])/3
print (average_price)
###e.4
print (favorite[2]<1900)
##
###e.5
still_another= still_another._replace(price=26)
print ("$", still_another.price, ".00")
##
###e.6
still_another = still_another._replace(price = (still_another[3] *1.2))
print("$", still_another.price)
##
#f
from collections import namedtuple
Animal = namedtuple('Animal', 'name species age weight food')
animal1= Animal('Jumbo', 'elephant', 50, 1000, 'peanuts')
animal2 = Animal('Perry', 'platypus', 7, 1.7, 'shrimp')
print(animal1[3] < animal2[3])
#print(animal1[1])

###g
print()
print("G")
booklist = [favorite, another, still_another]
print(booklist[0][3]<booklist[1][3])
#print(booklist[0][0])
print(booklist[0][2]>booklist[-1][2])

                        
#h
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

#h.1
print (RC[2][0])

#h.2
print(RC[0][1] == RC[3][1])

#h.3
print("$", RC[-1][4])

#h.4
RC.sort()
print(RC)

#h.5
print()
print(RC[-1].dish)

RC.sort()
print(RC)
print()
#h.6
RC.sort()
print()
new_list = [RC[0], RC[1], RC[-2], RC[-1]]
print(new_list)

#h.7

#i

import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

##my_canvas.create_line(100, 100, 300, 300, fill='orange') # Draw orange line
##my_canvas.create_line(300, 100, 100, 300, fill='blue')   # Draw blue line


#i1
my_canvas.create_line(100, 100, 100, 300, fill='orange')
my_canvas.create_line(100, 100, 300, 100, fill='orange')
my_canvas.create_line(300, 100, 300, 300, fill='orange')
my_canvas.create_line(100, 300, 300, 300, fill='orange')

#i2
my_canvas.create_line(200, 100, 300, 200, fill='orange')
my_canvas.create_line(100, 200, 200, 100, fill='orange')
my_canvas.create_line(300, 200, 200, 300, fill='orange')
my_canvas.create_line(100, 200, 200, 300, fill='orange')

###i3

my_canvas.create_line(100, 100, 100, 300, fill='orange')
my_canvas.create_line(100, 100, 300, 100, fill='orange')
my_canvas.create_line(300, 100, 300, 300, fill='orange')
my_canvas.create_line(100, 300, 300, 300, fill='orange')
my_canvas.create_line(100, 100, 200, 50, fill='orange')
my_canvas.create_line(200, 50, 300, 100, fill='orange')
my_canvas.create_rectangle(150, 150, 180, 180, fill='black')
my_canvas.create_rectangle(220, 200, 260, 300, fill='red')


###i4
my_canvas.create_oval(100, 100, 300, 300, fill='brown')
my_canvas.create_oval(150, 150, 250, 250, fill='black')
##
#i5
#smartphone
my_canvas.create_rectangle(100, 100, 300, 500)
my_canvas.create_rectangle(120, 120, 280, 430)
my_canvas.create_oval(180, 450, 220, 490)
tkinter.mainloop()          # Combine all the elements and display the window



