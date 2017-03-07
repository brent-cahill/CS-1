import random
# Ex B.1:
def complement(a):
    """
    Returns the "complement" of a letter DNA sequence. Takes an argument
    a, which should be a string. The output represents the DNA nucleotide
    complement of any DNA sequence
    """
    comp = ''
    for w in a:
        if w == 'A':
            comp += 'T'
        elif w == 'T':
            comp += 'A'
        elif w == 'C':
            comp += 'G'
        elif w == 'G':
            comp += 'C'
    return comp

# Ex B.2:
def list_complement(b):
    """
    Changes the nucleotide of a list DNA sequence to its "complement." Takes an
    argument b, which should be a list of strings. There is no output.
    """
    for w in range (len(b)):
        if b[w] == 'A':
            b[w] = 'T'
        elif b[w] == 'T':
            b[w] = 'A'
        elif b[w] == 'C':
            b[w] = 'G'
        elif b[w] == 'G':
            b[w] = 'C'

# Ex B.3:
def product(c):
    """
    Returns the product of a list of numbers. Takes an argument c, which should
    be a list of integers.
    """
    prod = 1
    for p in c:
        prod *= p
    return prod

# Ex. B.4:
def factorial(d):
    """
    Returns the factorial of an integer argument d.
    """
    return product(range(1, d + 1))
    
# Ex. B.5:
def dice(m, n):
    """
    Returns the sum of n number of pseudo-random dice rolls with dice with m
    sides. Takes two integer arguments m and n, the number of sides on the die
    and the number of times rolled, repectively.
    """
    numSum = 0
    for roll in range(n):
        numSum += random.choice(range(1, m + 1))
    return numSum

# Ex. B.6:
def remove_all(lst, value):
    """
    Removes all instances of an integer argument value from a list argument of
    integers (lst) by using a while loop (counting the number of times the value
    is in the list).
    """
    while lst.count(value) > 0:
        lst.remove(value)
        
# Ex. B.7.1:
def remove_all2(lst2, value2):
    """
    Removes all instances of an integer argument value from a list argument of
    integers (lst) by using a for loop.
    """
    removeNum = lst2.count(value2)
    for x in range(removeNum):
        lst2.remove(value2)
        
# Ex. B.7.2:
def remove_all3(lst3, value3):
    """
    Removes all instances of an integer argument value from a list argument of
    integers (lst) by using a while loop (checking if the value is in the list).
    """    
    while value3 in lst3:
        lst3.remove(value3)
        
# Ex. B.8:
def any_in(check1, check2):
    """
    Checks if any value in one list is equal to any value in a second list.
    Takes two arguments, check1 and check2, which should be lists. Returns a
    boolean.
    """
    for y in check1:
        if y in check2:
            return True
    return False

# Ex. C.1.a:
# The "third" line of code does not check to see if a is 0, it is syntactically
# incorrect. To check if a variable is equal to something, you must use a double
# equals sign. the line of code would be correct if it read as:
# if a == 0:

a = 20
# ... later in the program, test to see if a has become 0.
if a == 0:
    print 'a is zero!'

# Ex. C.1.b:
# The argument cannot have quotes around it. The argument can be a string, but
# if cannot have quotes around it to indicate that.

def add_suffix(s):
    '''This function adds the suffix '-Caltech' to the string s.'''
    return s + '-Caltech'

# Ex. C.1.c:
# This will return 's-Caltech' everytime, rather than the actual string s with
# '-Caltech' at the end, because there are quotes surrounding s in the return
# statement.

def add_suffix(s):
    '''This function adds the suffix '-Caltech' to the string s.'''
    return s + '-Caltech'

# Ex. C.1.d:
# You cannot concatenate a string element to a list. In order to add a value to
# to a list, you must use a method, namely list.append(x)

# We want to add the string 'bam' to a list of strings, changing the original
# list.
lst = ['foo', 'bar', 'baz']
lst.append('bam')

# Ex. C.1.e:
# The problem arrives when when you set a variable 'lst2' equal to lst.reverse()
# this is a method call, and does not return anything for lst2 to be assigned.
# It is also poor coding style to introduce another variable when one would
# suffice:
def reverse_and_append_zero(lst):
    '''This function reverses a list of numbers and then
    appends the number 0 to the end of the list.'''
    lst.reverse()
    lst.append(0)

# Ex. C.1.f:
# You cannot call a variable list. Moreover, appending a list to a list would
# result in a list within a list. To fix this, you could instead write:
def append_string_letters_to_list(lst, strin):
    '''This function converts a string 'str' to a list and appends
    the letters of the string to the list 'list'.'''
    a = list(strin)
    for char in a:
        lst.append(char)
        
# Ex. C.2:
# the following code will print 30 instead of 50:
# a = 10
# b = 20
# c = b + a
# a = 30
# print c
# we will run through these lines of code step by step, as the computer would:
# First, variable a is assigned a value 10.
# Then, variable b is assigned a value of 20.
# Next, variable c is assigned a value of b + a, which is 30.
# Finally, variable a is assigned a value of 30.
# We then print the value of c.
# Note that a variable can only be assigned a value in the following syntax:
# variable = value
# So, since c is only assigned a value once (30), it can only print out 30.

# Ex. C.3:
# Printing a result (as in add_and_double_2(x, y, z)), would not work, because
# it is used to simply print out the result of whatever is within the function
# to the shell. It cannot be used as a value. When a result is returned, it is
# treated as a value that can be operated on.

# Ex. C.4:
# The second one (sum_of_squares_2(2, 3)) would not work because it is passed
# arguments, even though the function does not have any arguments to be passed.
# The first would work because the arguments work within the actual function.
# Getting values from raw_input is different from putting a variable in the
# arguments of a function because the variables are assigned after the function
# has begun to run in the shell. Python will prompt the user for an imput and
# the variable will be assigned after the user inputs.

# Ex. C.5:
# You cannot write a value of a string at an index by using an equals sign
# because a string is an immutable object. You would simply write:
def capitalize(s):
    '''This function capitalizes the first letter of the string 's'.'''
    s = list(s)
    s[0] = s[0].upper()
    ''.join(s)

# Ex. C.6:
# This will not work because in each iteration of the for loop, the variable
# named item is doubled, but never stored into the list, thus the function will
# not change the list at all.

def double_list(lst):
    '''This function doubles each element in a list in-place.'''
    for item in range(len(lst)):
        lst[item] *= 2