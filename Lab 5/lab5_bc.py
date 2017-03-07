import math

# Problem B.1:
class Point:
    """
    This class defines a point in 3D Euclidian geometry
    """
    def __init__(self, xval, yval, zval):
        '''Constructs an object of class point'''
        self.xvalue = xval
        self.yvalue = yval
        self.zvalue = zval
        
    def distanceTo(self, pt):
        """
        Returns the distance to another point in 3D coordinate space
        """
        xval = self.xvalue
        yval = self.yvalue
        zval = self.zvalue
        xval2 = pt.xvalue
        yval2 = pt.yvalue
        zval2 = pt.zvalue
        return math.sqrt((xval - xval2)**2 + (yval - yval2)**2 + 
                             (zval - zval2)**2)

# Problem B.2:
class Triangle:
    """
    This class defines a triangle in 3D Euclidian geometry.
    """
    def __init__(self, pt1, pt2, pt3):
        '''Constructs an object of class triangle'''
        self.value1 = pt1
        self.value2 = pt2
        self.value3 = pt3
        
    def area(self):
        """Returns the area of the triangle in 3D, using the distanceTo method
        from the point class above"""
        pt1 = self.value1
        pt2 = self.value2
        pt3 = self.value3
        side1 = pt1.distanceTo(pt2)
        side2 = pt2.distanceTo(pt3)
        side3 = pt3.distanceTo(pt1)
        per = (side1 + side2 + side3) / 2
        return math.sqrt(per * (per - side1) * (per - side2) * (per - side3))

# Problem B.3:
class Averager:
    """
    This class stores a list of numbers and performs various operations on it.
    """
    def __init__(self):
        '''Constructs an object of class Averager'''
        self.nums = []
        self.total = 0.0
        self.n = 0.0
        self.minim = 0
        self.maxim = 0
    
    def getNums(self):
        '''Returns the numbers in the list'''
        return self.nums[:]
    
    def append(self, num):
        '''Adds a single number 'num' to the end of the list'''
        self.nums.append(num)
        self.total += num
        self.n += 1
        if self.n == 1:
            self.maxim = num
            self.minim = num
        if num > self.maxim:
            self.maxim = num
        elif num < self.minim:
            self.minim = num      
    
    def extend(self, lst2):
        '''Adds the elements of a list 'lst2' to the end of the list'''
        for i in lst2:           
            self.nums.append(i)
            self.total += i
            self.n += 1
            if self.n == 1:
                self.maxim = i
                self.minim = i
            if i > self.maxim:
                self.maxim = i
            elif i < self.minim:
                self.minim = i
    
    def average(self):
        '''Returns the mean of the list'''
        if self.n == 0:
            return 0.0
        else:
            return self.total / self.n
        
    def limits(self):
        '''Returns the minimum and maximum of the list'''
        return(int(self.minim), int(self.maxim))
    
# Problem C.1:
def is_positive(x):
    '''Test if x is positive.'''
    if x > 0:
        return True
    else:
        return False
    
# This function is unnecessarily long, you can complete it with one statement:
def is_positive(x):
    '''Test if x is positive.'''
    return x > 0

# Problem C.2:
def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    found = False
    location = -1
    for i, item in enumerate(lst):
        if item == x:
            found = True
            location = i
    if found == True:
        return location
    else:
        return -1

# This function does not need to declare found or location, nor does it need
# either of those variables. It was unnecessarily long, this is a better
# way to write it:
def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    for i, item in enumerate(lst):
        if item == x:
            return i
    return -1

# Problem C.3:
def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''
    if x < 0:
        category = 'negative'
    if x == 0:
        category = 'zero'
    if x > 0 and x < 10:
        category = 'small'
    if x >= 10:
        category = 'large'
    return category

# This function utalizes too many if statements, it can be solved without using
# so many, and a return statement ends the if statement, so you don't need else
# statements, lastly, you don't need to set a variable equal to anything, you
# can simply return the string. Unnecessary code / unnecessarily complex code.
def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''
    if x < 0:
        return 'negative'
    if x > 0:
        if x >= 10:
            return 'large'
        return 'small'
    return 'zero'

# Problem 3.4:
def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''

    if len(lst) == 0:
        answer = 0
    elif len(lst) == 1:
        answer = lst[0]
    elif len(lst) == 2:
        answer = lst[0] + lst[1]
    elif len(lst) > 2:
        total = 0
        for item in lst:
            total += item
        answer = total
    return answer

# There is no need for the if statements, the for loop already handles those
# cases. Unnecessary code.
def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''
    total = 0
    for item in lst:
        total += item
    return total