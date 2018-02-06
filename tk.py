import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

##my_canvas.create_line(100, 100, 300, 300, fill='orange') # Draw orange line
##my_canvas.create_line(300, 100, 100, 300, fill='blue')   # Draw blue line


#i1
##my_canvas.create_line(100, 100, 100, 300, fill='orange')
##my_canvas.create_line(100, 100, 300, 100, fill='orange')
##my_canvas.create_line(300, 100, 300, 300, fill='orange')
##my_canvas.create_line(100, 300, 300, 300, fill='orange')

#i2
##my_canvas.create_line(200, 100, 300, 200, fill='orange')
##my_canvas.create_line(100, 200, 200, 100, fill='orange')
##my_canvas.create_line(300, 200, 200, 300, fill='orange')
##y_canvas.create_line(100, 200, 200, 300, fill='orange')

#i3

##my_canvas.create_line(100, 100, 100, 300, fill='orange')
##my_canvas.create_line(100, 100, 300, 100, fill='orange')
##my_canvas.create_line(300, 100, 300, 300, fill='orange')
##my_canvas.create_line(100, 300, 300, 300, fill='orange')
##my_canvas.create_line(100, 100, 200, 50, fill='orange')
##my_canvas.create_line(200, 50, 300, 100, fill='orange')
##my_canvas.create_rectangle(150, 150, 180, 180)
##my_canvas.create_rectangle(220, 200, 260, 300, fill='red')


###i4
##my_canvas.create_oval(100, 100, 300, 300, fill='brown')
##my_canvas.create_oval(150, 150, 250, 250, fill='black')
##
#i5
#smartphone
my_canvas.create_rectangle(100, 100, 300, 500)
my_canvas.create_rectangle(120, 120, 280, 430)
my_canvas.create_oval(180, 450, 220, 490)
tkinter.mainloop()          # Combine all the elements and display the window


