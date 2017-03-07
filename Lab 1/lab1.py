# Brent Cahill
# CS1 Problem Set 1


# Ex C.1.1: 9 - 3 --> 6
# Ex C.1.2: 8 * 2.5 --> 20.0
# Ex C.1.3: 9 / 2 --> 4
# Ex C.1.4: 9 / -2 --> -5
# Ex C.1.5: 9 % 2 --> 1
# Ex C.1.6: 9 % -2 --> -1
# Ex C.1.7: -9 % 2 --> 1
# Ex C.1.8: 9 / -2.0 --> -4.5
# Ex C.1.9: 4 + 3 * 5 --> 19
# Ex C.1.10: (4 + 3) * 5 --> 35

# Ex C.2.1 x = 100 will assign the value of 100 to the variable x
# Ex C.2.2 x = x + 10 will assign the value of 110 to the variable x
# Ex C.2.3 x += 20 will assign the value of 130 to the variable x
# Ex C.2.4 x = x - 40 will assign the value of 90 to the variable x
# Ex C.2.5 x -= 50 will assign the value of 40 to the variable x
# Ex C.2.6 x *= 3 will assign the value of 120 to the variable x
# Ex C.2.7 x /= 5 will assign the value of 24 to the variable x
# Ex C.2.8 x %= 3 will assign the value of 0 to the variable x

# Ex C.3
# x = 3
# x += x - x
# The revious two lines of code will assign a value of 3 to the variable x in
# the following manner:
# The computer will evaluate the right side of the equation: x - x as
# (3) - (3) first, which equals 0, then it will add that value to the
# variable on the left side of the equation.

# Ex C.4.1.1: 1j + 2.4j --> 3.4j
# Ex C.4.1.2: 4j * 4j --> (-16+0j)
# Ex C.4.1.3: (1+2j) / (3+4j) --> (0.44+0.08j)

# Ex C.4.2.1: (1+2j) * (1+2j) --> (-3+4j)
# Ex C.4.2.2: 1+2j * 1+2j --> (1+4j)
# These answers are different because python will always evaluate a
# multiplication statement before an addition statement, even if there is no
# space between the addition sign and the numbers, and also even if the number
# is an imaginary number

from math import *
print sin(-1.0)

# Ex C.5.1: cmath.sin(-1.0+2.0j) --> (-3.16577851322+1.95960104142j)
# Ex C.5.2: cmath.log(-1.0+3.4j) --> (1.26525858052+1.85684776851j)
# Ex C.5.3: cmath.exp(-cmath.pi * 1.0j) --> (-1-1.22464679915e-16j)
# Import math and import cmath would be a better idea than from math import *
# and from cmath import * because the first two statements would allow for the
# programmer to use math.[function] as opposed to simply [function], which might
# get confusing. It also would import every function in math or cmath, which is
# an unnecessary burden on the program. The former also forces python to use
# whichever was imported later for functions that are not expressely library
# defined. For example, the statement:
# from math import *
# from cmath import *
# print sin(-1.0)
# would return --> (-0.8414709848078965+0j)
# which is the cmath evaluation of sin(-1.0)

# Ex C.6.1: "foo" + 'bar' --> 'foobar'
# Ex C.6.2: "foo" 'bar' --> 'foobar'
# Ex C.6.3:
# a = 'foo'
# b = "bar"
# a + b --> 'foobar'
# Ex C.6.4:
# a = 'foo'
# b = "bar"
# a + b --> Traceback (most recent call last):
#   Python Shell, prompt 1, line 65
# invalid syntax: <string>, line 65, pos 9

# Ex. C.7:
# 'A \nB \nC'

# Ex. C.8: print '-' * 80

# Ex. C.9: "first line \nsecond line \nthird line"

# Ex C.10:
x = 3
y = 12.5
print "The rabbit is %d." %x
print "The rabbit is %d years old." %x
print "%.1f is average." %y
print "%.1f * %d." % (y, x)
print "%.1f * %d is %.1f." %(y, x, y * x)

# Ex. C.11:
num = float(raw_input("Enter a number: "))
print num

# Ex. C.12:
def quadratic(a, b, c, x):
  return a * x ** 2 + b * x + c

# Ex C.13:
def GC_content(a):
  """
  Returns the proportion of 'G' and 'C' in a DNA sequence to the entirety of
  the sequence, regardless of letter case. Argument 'a' should be a string.
  The output represents the percentage of 'Guanine' and 'Cytosine' in the
  inputted DNA sequence.
  """
  g = a.count('G') # counts the instances of 'G'
  c = a.count('C') # counts the instances of 'C'
  return float((g + c)) / float(len(a))
  # The above line converts the total number of 'G' and 'C' (g + c) into a float
  # then divides it by the length of the string (also converted to a float)

