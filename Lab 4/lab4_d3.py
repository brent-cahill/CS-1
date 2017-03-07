from Tkinter import *
import random

def random_size(a, b):
    """
    Takes 2 nonnegative even integers 'a' and 'b', where a < b, and returns
    a random even int >= a and <= b.
    """
    assert a >= 0 and b >= 0, 'inputs positive'
    assert a % 2 == 0 and b % 2 == 0, 'inputs even'
    assert a < b, 'first input smaller'
    rand = 2 * random.randint(a / 2, b / 2)
    assert rand % 2 == 0, 'output even'
    return rand

def random_position(max_x, max_y):
    """
    Takes 2 nonnegative integers 'max_x' and 'max_y' and returns a random tuple
    within those bounds
    """
    assert max_x >= 0 and max_y >= 0
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    return (x, y)

def random_color():
    """
    Returns a random hexadecimal color
    """
    color = '#'
    for i in range(6):
        color += random.choice('0123456789abcdef')
    return color

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
    c.pack()
    for i in range(60):
        draw_square(c, random_color(), random_size(20, 150),
                    random_position(800, 800)[0], random_position(800, 800)[1])
    root.bind('q', quit)
    root.mainloop()