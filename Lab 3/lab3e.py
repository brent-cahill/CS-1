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

# Plant
plant = { 'start' : 'X', 
          'X'     : 'F-[[X]+X]+F[+FX]-X', 
          'F'     : 'FF' }

plant_draw = { 'F' : 'F 1', 
               '-' : 'L 25', 
               '+' : 'R 25' }

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
    i = 0
    lList = list(lstr)
    while i != len(lList):
        if lList[i] in lsys:
            lList[i] = lsys[lList[i]]
        i += 1
    return ''.join(lList)

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
    s = list(s)
    x = 0.0
    y = 0.0
    ang = 0.0
    for i in range(len(s)):
        if s[i] == '[':
            for i in range(len(drawList)):
                loc = nextLocation(x , y, ang, drawList[i])
                x = loc[0]
                y = loc[1]
                ang = loc[2]
        elif s[i] == ']':
            drawList.append('G' + ' ' + str(loc[0]) + ' ' + str(loc[1]) + ' '
                            + str(loc[2]))
        if s[i] in draw:
            drawList.append(draw[s[i]])
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
    for i in range(len(cmds)):
        loc = nextLocation(x , y, ang, cmds[i])
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
    extraList = []
    if cmd[0] == 'F':
        locx += float(cmd[1]) * math.cos(ang * (math.pi / 180))
        locy += float(cmd[1]) * math.sin(ang * (math.pi / 180))
    elif cmd[0] == 'R':
        ang -= int(cmd[1])
    elif cmd[0] == 'L':
        ang += int(cmd[1])
    if ang < 0:
        ang = 360 + ang    
    if cmd[0] == '[':
        extraList.append(locx)
        extraList.append(locy)
        extraList.append(ang)
    elif cmd[0] == ']':
        locx = extraList.pop(0)
        locy = extraList.pop(0)
        ang = extraList.pop(0)
    return locx, locy, ang

def saveDrawing(filename, bounds, cmds):
    """
    Will write bounds and cmds to the file 'filename' by first writing the
    bounds information on a single line, and then by writing the drawing
    commands to the file, one per line.
    """
    filename = open(filename, 'w')
    filename.write(str(bounds[0]) + ' ' + str(bounds[1]) + ' ' + str(bounds[2])
                   + ' ' + str(bounds[3]) + '\n')
    for i in range(len(cmds)):
        filename.write(cmds[i] + '\n')
    

def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print 'Making drawings for %s...' % name
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('plant', plant, plant_draw, 0, 6)

