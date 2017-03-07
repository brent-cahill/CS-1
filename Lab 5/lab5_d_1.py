from Tkinter import *
import random

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

def draw_random_circle(posx, posy):
    """
    Creates a circle
    """
    diam = random.choice(range(10,50))
    return canvas.create_oval(posx - diam / 2, posy - diam / 2, posx +
                              diam / 2, posy + diam / 2, fill = color,
                              outline = color)


# Event handlers.

def key_handler(event):
    '''Handles key presses.'''
    global circList
    key = event.keysym
    if key == 'q':
        quit()
    if key == 'c':
        color = random_color()
    if key == 'x':
        for i in circList:
            canvas.delete(i)
        circList = []        
        
def button_handler(event):
    '''Handle left mouse button click events.'''
    circle = draw_random_circle(event.x, event.y)
    circList.append(circle)
    return circle        

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    random_color()
    circList = []
    #<your code goes here>

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()

