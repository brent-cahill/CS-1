'''
lab3d.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 

def update(lsys, lstr):
    """
    Generates the next version of the L-system string by applying the L-system
    rules to each char of the string and combining all the strings into one big
    string. Any character which is not a key in the L-system dictionary is
    copied into the new string unchanged.
    """
    newStr = ''
    for i in lstr:
        if i in lsys:
            newStr += lsys[i]
        else:
            newStr += i
    return newStr

def iterate(lsys, n):
    """
    Returns the string which results from starting with the starting string
    for that L-system and updating n times
    """
    string = lsys['start']
    for x in range(n):
        string = update(lsys, string)
    return string

def lsystemToDrawingCommands(draw, s):
    """
    Returns the list of drawing commands needed to draw the figure corresponding
    to the L-system string.
    """
    drawList = []
    for i in s:
        if i in draw:
            drawList.append(draw[i])
    return drawList

def bounds(cmds):
    """
    Computes the bounding coordinates of the resulting drawing.
    """
    maxx = 0.0
    maxy = 0.0
    minx = 0.0
    miny = 0.0
    x = 0.0
    y = 0.0
    ang = 0.0
    for i in cmds:
        loc = nextLocation(x , y, ang, i)
        x = loc[0]
        y = loc[1]
        if loc[0] > maxx:
            maxx = loc[0]
        elif loc[0] < minx:
            minx = loc[0]
        if loc[1] > maxy:
            maxy = loc[1]
        elif loc[1] < miny:
            miny = loc[1]
        ang = loc[2]
    return (minx, maxx, miny, maxy)

def nextLocation(x, y, angle, cmd):
    """
    Generates the next location and direction of the turtle after that drawing
    command has executed. Returns tuple of three values, the next x coordinate
    of the turtle, the next y coordinate, and the next angle. The x and y values
    are floating-point numbers.
    """
    locx = x
    locy = y
    ang = angle
    cmd = cmd.split()
    if cmd[0] == 'F':
        locx += float(cmd[1]) * math.cos(ang * (math.pi / 180))
        locy += float(cmd[1]) * math.sin(ang * (math.pi / 180))
    elif cmd[0] == 'R':
        ang -= int(cmd[1])
    elif cmd[0] == 'L':
        ang += int(cmd[1])
    ang = ang % 360
    return locx, locy, ang

def saveDrawing(filename, bounds, cmds):
    """
    Will write bounds and cmds to the file 'filename' by first writing the
    bounds information on a single line, and then by writing the drawing
    commands to the file, one per line.
    """
    fyle = open(filename, 'w')
    fyle.write(str(bounds[0]) + ' ' + str(bounds[1]) + ' ' + str(bounds[2])
               + ' ' + str(bounds[3]) + ' ' '\n')
    for i in cmds:
        fyle.write(i + '\n')
    fyle.close()
    

def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print 'Making drawings for %s...' % name
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)

