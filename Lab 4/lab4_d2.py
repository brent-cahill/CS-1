from Tkinter import *
def draw_square(can, colr, side, x , y ):
    """
    Takes 4 arguments, the canvas, the color of the square, the side length of
    the square, and the center of the square in x,y positions. Creates a square
    with the given parameters.
    """
    c = can
    c.pack()
    vertx_1 = x - (side / 2)
    verty_1 = y - (side / 2)
    vertx_2 = x + (side / 2)
    verty_2 = y + (side / 2)    
    r1 = c.create_rectangle(vertx_1, verty_1, vertx_2, verty_2, fill=colr,
                            outline=colr)
    return r1

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    c = Canvas(root, width=800, height=800)
    draw_square(c, 'red', 100, 50, 50)
    draw_square(c, 'green', 100, 750, 50)
    draw_square(c, 'blue', 100, 50, 750)
    draw_square(c, 'yellow', 100, 750, 750)
    root.mainloop()
    