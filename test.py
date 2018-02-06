import tkinter              # Load the library; do this just once per program
##
my_window = tkinter.Tk()    # Create the graphics window
##
my_canvas = tkinter.Canvas(my_window, width=750, height=750)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window


def draw_eye(x_start2, y_start2, x_end2, y_end2, color):
    my_canvas.create_oval(x_start2, y_start2, x_end2, y_end2, fill=color)
    my_canvas.create_oval(x_start2 + 50, y_start2+50, x_end2-10, y_end2-10, fill='black')

#draw_eye(100, 100, 300, 300, 'brown')
#draw_eye(400, 100, 600, 300, 'brown')
def draw_nose(x1, y1, x2, y2, color):
    my_canvas.create_line(x1, y1, x2, y2, fill=color)
    my_canvas.create_line(x1, y1, x2, y2, fill=color)
    my_canvas.create_line(x1, y1, x2, y2, fill=color)
##draw_nose(300, 400, 400, 400, 'brown')
##draw_nose(350, 300, 400, 400, 'brown')
#draw_nose(350, 300, 300, 400, 'brown')

def draw_mouth(x4, y4, x5, y5):
       my_canvas.create_oval(x4, y4, x5, y5, fill='red')
#draw_mouth(300, 500, 400, 600)
           

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

