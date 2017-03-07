# Ex. B.1:
def union(set1, set2):
    union = set2
    for i in set1:
        if i not in set2:
            union.add(i)
    return union

# Ex. B.2:
def intersection(set1, set2):
    union = set()
    for i in set1:
        if i in set2:
            union.add(i)
    return union

# Ex. B.3:
def mySum(*nums):
    summ = 0
    for i in nums:
        if i < 0:
            raise ValueError('Argument is less than 0')
        if type(i) is not int:
            raise TypeError('Argument is not an integer')
    for i in nums:
        summ += i
    return summ

# Ex. B.4:
def myNewSum(*nums):
    summ = 0
    if len(nums) == 1:
        if type(nums[0]) is not list and type(nums[0]) is not int:
            raise TypeError('Argument is not an integer or a list')
        if type(nums[0]) is list:
            for i in nums[0]:
                if type(i) is not int:
                    raise TypeError('List element is not an integer')
                if i <= 0:
                    raise ValueError('List element is less than 1')                
                summ += i
        else:
            return nums[0]
        return summ
    else:
        for i in nums:
            if i <= 0:
                raise ValueError('Argument is less than 1')
            if type(i) is not int:
                raise TypeError('More than one argument, \
argument is not an integer')
        for i in nums:
            summ += i
        return summ
    
# Ex. B.5:
def myOpReduce(lst, **kw):
    pi = 1    
    if len(kw) == 0:
        raise ValueError('no keyword argument')
    if 'op' not in kw:
        raise ValueError('invalid keyword argument')
    if type(kw['op']) is not str:
        raise TypeError("value for keyword argument 'op' must be a string")    
    if len(kw) > 1:
        raise ValueError('too many keyword arguments')
    if kw['op'] != '+' and kw['op'] != '*' and kw['op'] != 'max':
        raise ValueError('invalid keyword argument')        
    if kw['op'] == '+':
        return sum(lst)
    elif kw['op'] == '*':
        for i in lst:
            pi *= i
        return pi
    elif kw['op'] == 'max':
        if len(lst) == 0:
            return 0
        return max(lst)
    
# Ex. C.1:
# There is no quit() defined for this function. It should read as pass instead.
# You also do not need to import sys, and you should print an error message
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:
        print 'key not found!'

# Ex. C.2:
# You do not need to print out the error message as a standard error, nor import
# sys
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:   # raised if a key isn't in a dictionary
        print 'key not found!'
        
# Ex. C.3:
# You should print an error message and there is no use in raising a KeyError if
# it is within an except KeyError statement.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:   # raised if a key isn't in a dictionary
        print 'key not found!'
        
# Ex. C.4:
# You can write the try statements in one try statement to avoid getting
# incorrect final return statements if only on try statement fails. This way,
# if one fails, both fail.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        val1 = dict[key1]
        val2 = dict[key2]
        return val1 + val2
    except KeyError, e:   
        raise e

# Ex. C.5:
# The print >> sys.stderr line will never be reached because we raise an error
# before it.
import sys

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        print >> sys.stderr, 'n must be >= 0'
        raise ValueError
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)
    
# Ex. C.6:
# This is better because it informs the user of what Error was raised as well as
# the error message
import sys

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        print >> sys.stderr
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)
    
# Ex. C.7:
# x cannot equal 0 either, as this will result in ZeroDivisionError.
from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if x <= 0:
        raise TypeError('x must be > 0.0')
    return (exp(x) / x)

# Ex. C.8:
# These should not be Exceptions, they should be certain types of Errors.
from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if type(x) is not float:
        raise TypeError('x must be a float')
    elif x <= 0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)
