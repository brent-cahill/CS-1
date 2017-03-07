'''
This module simulates balls bouncing around a canvas.
'''

import math
import random
from Tkinter import *

class BouncingBall:
    '''Objects of this class represent balls which bounce on a canvas.'''
    def __init__(self, canvas, center, radius, color, direction, speed):
        '''Create a new ball at center of the given radius and color, 
        moving at a given direction and speed.'''

        x, y = center
        x1 = x - radius
        y1 = y - radius
        x2 = x + radius
        y2 = y + radius
        self.handle = canvas.create_oval(x1, y1, x2, y2,
                        fill=color, outline=color)
        self.canvas = canvas
        self.xmax   = int(canvas.cget('width')) - 1
        self.ymax   = int(canvas.cget('height')) - 1
        self.center = center
        self.radius = radius
        self.color  = color

        # The direction is represented as an angle in degrees
        # (range 0-360), which we convert to radians here.
        # The angle is with respect to the positive x axis,
        # going clockwise around the origin.
        if direction < 0.0 or direction > 360.0:
            raise ValueError('Invalid direction; must be in range [0.0, 360.0]')
        dir_radians = direction * math.pi / 180.0

        # Separate the direction into its x and y coordinates.
        # Flip the sign of the y coordinate because the y coordinate
        # grows downward, not upward.
        self.dirx = math.cos(dir_radians)
        self.diry = -math.sin(dir_radians)

        # Speed is represented as a single non-negative float.
        # Note that non-float speeds will behave poorly.
        if speed < 0.0: 
            raise ValueError('Invalid speed; must be positive')
        self.speed = speed

    def step(self):
        '''Move this ball in its current direction with its
        current speed.  Change direction if the edge of the
        canvas is reached.'''

        xchange, direction = self.displacement(self.center[0], self.speed *
                                          self.dirx, self.xmax)
        self.dirx *= direction
        ychange, direction = self.displacement(self.center[1], self.speed *
                                          self.diry, self.ymax)
        self.diry *= direction
        self.center = (self.center[0] + xchange, self.center[1] + ychange)
        self.canvas.move(self.handle, xchange, ychange)
    def displacement(self, c, d, cmax):
        '''Compute the actual displacement along the x or y dimension,
        taking reflections off the edge into account.  'c' is the
        center of the ball (x or y coordinate); 'cmax' is the largest 
        value in that direction, and 'd' is the desired displacement
        in that direction.'''

        if c + d > cmax - self.radius:
            return (2 * (cmax - self.radius - c) - d, -1)
        if c + d < self.radius:
            return (-.00000000000001, -1)
        return (d, 1)

    def scale_speed(self, scale):
        '''Scale the speed of this object by a factor 'scale'.'''
        self.speed *= scale

    def delete(self):
        '''Remove this object from the canvas.'''
        self.canvas.delete(self.handle)


def random_ball(canvas, rmin, rmax, smin, smax, xmax, ymax):
    '''
    Create and return a ball with a random color, starting position,
    size, direction, and velocity.
    rmin: minimum radius (pixels)
    rmax: maximum radius (pixels)
    smin: minimum speed
    smax: maximum speed
    xmax: maximum x dimension of canvas
    ymax: maximum y dimension of canvas
    '''
    color = '#'
    for i in range(6):
        color += random.choice('0123456789abcdef')
    radius = random.randint(rmin, rmax)
    speed = float(random.randint(smin, smax))
    cx = random.randint(radius, xmax - radius)
    cy = random.randint(radius, ymax - radius)
    direction = random.randint(0, 360)
    return BouncingBall(canvas, (cx, cy), radius, color, direction, speed)

def key_handler(event):
    '''Handle key presses.'''
    global bouncing_balls
    global done
    key = event.keysym
    if key == 'q': 
        done = True
    elif key == 'plus':  # add a ball at a random location
        bouncing_balls.append(random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600))
    elif key == 'minus':  # remove a ball from the canvas if there are any
        if bouncing_balls != []:
            bouncing_balls[-1].delete()
            del bouncing_balls[-1]
    elif key == 'u':  # speed (u)p all bouncing_balls by factor of 1.2
        for i in bouncing_balls:
            i.scale_speed(1.2)
    elif key == 'd':  # slow (d)own all bouncing_balls by factor of 1.2
        for i in bouncing_balls:
            i.scale_speed(0.8)
    elif key == 'x':  # delete all bouncing_balls
        for i in bouncing_balls:
            i.delete()

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()
    done = False

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    
    # Set up some bouncing balls.
    bouncing_balls = []
    for i in range(5):
        bouncing_balls.append(random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600))

    # Start the event loop.
    while not done:
        for ball in bouncing_balls:
            ball.step()
        root.update()

