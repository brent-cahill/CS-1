from Tkinter import *
import random
import math

# Graphics commands.

def random_color():
    """
    Returns a random hexadecimal color
    """
    global color
    color = '#'
    for i in range(6):
        color += random.choice('0123456789abcdef')
    return color

def draw_line(pos1, pos2):
    """
    Creates a line between points pos1 and pos2
    """
    line = canvas.create_line(pos1[0], pos1[1], pos2[0], pos2[1], fill = color)
    return line

def draw_star(cPos):
    """
    Creates a star with random 'diameter' between 50 and 100 px with n verteces
    with a center at cPos
    """
    radius = random.choice(range(50, 100))
    edges = []
    points = []
    for i in range(n):
        theta = i * (2 * math.pi / n)
        points.append((cPos[0] + radius * math.sin(theta),
                      cPos[1] - radius * math.cos(theta)))
    connect = (n - 1) / 2
    for i in range(len(points)):
        line = draw_line(points[i], points[(i + connect) % n])
        edges.append(line)
    return edges

# Event handlers.

def key_handler(event):
    '''Handles key presses.'''
    global starList
    global color
    global n
    key = event.keysym
    if key == 'q':
        quit()
    if key == 'c':
        color = random_color()
    if key == 'x':
        for i in starList:
            canvas.delete(i)
        starList = []
    if key == 'plus':
        n += 2
    if key == 'minus':
        if n != 5:
            n -= 2
        
def button_handler(event):
    '''Handle left mouse button click events.'''
    global starList
    star = draw_star((event.x, event.y))
    starList += star      

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    starList = []
    edges = []
    points = []
    color = random_color()
    n = 5

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()

