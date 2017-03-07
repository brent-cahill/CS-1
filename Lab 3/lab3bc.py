def list_reverse(lst):
    """
    Reverses the elements of a list 'lst'
    """
    lst2 = lst[:]
    lst2.reverse()
    return lst2

def list_reverse2(lst):
    """
    Reverses the elements of a list 'lst'
    """
    lst2 = []
    for x in range(len(lst) - 1, -1, -1):
        lst2.append(lst[x])
    return lst2

def file_info(fle):
    """
    Returns the number of lines, number of words and number of characters in a
    file 'fle'
    """
    fyle = open(fle, 'r')
    words = 0
    lines = 0
    characters = 0
    while True:       
        line = fyle.readline()
        if line == '':
            break        
        lines += 1
        words += len(line.split())
        characters += len(line)
    fyle.close()
    return (lines, words, characters)

def file_info2(fyle):
    """
    Inserts the information from file_info into a dictionary with keys
    corresponding to the information.
    """
    info = {}
    lines, words, chars = file_info(fyle)
    info = {'lines' : lines, 'words' : words, 'characters' : chars}
    return info

def longest_line(fle):
    """
    Determines the length and contents of the longest line in a file 'fle'
    """
    fyle = open(fle, 'r')
    maxLen = 0
    line = ''
    for lines in fyle:
        if (len(lines)) > maxLen:
            maxLen = len(lines)
            line = lines
    fyle.close()
    return (maxLen, line)

def sort_words(string):
    newList = string.split()
    newList.sort()
    return newList

# Ex. B.7: Binary to decimal -> 11011010 -> (0 * 2^0) + (1 * 2^1) + (0 * 2^2) +
# (1 * 2^3) + (1 * 2^4) + (0 * 2^5) + (1 * 2^6) + (1 * 2^7) = 218
# it is equal to the sum from i = 0 to n of (i * 2^n) where i = the (n-1) th
# digit of the binary number.
# The largest 8 digit binary number is 11111111 = 255 in decimal

def binaryToDecimal(binary):
    decimal = 0
    for x in range(len(binary)):
        decimal += binary[x] * (2 ** (len(binary) - (x + 1)))
    return decimal

# Honor Roll Problem
def binary_list_maker(n):
    binary = []
    for x in range(n):
            binary.append(0)
    return binary

def decimalToBinary(decimal):
    binary = []
    flag = True
    while True:
        n = 0
        while True:
            if 2 ** n < decimal:
                n += 1
            elif 2 ** n == decimal :
                if flag == True:
                    binary = binary_list_maker(n + 1)
                    binary[0] = 1
                if flag == False:
                    binary[len(binary) - 1 - (n)] = 1
                decimal -= 2 ** n
                break
            else:
                if flag == True:
                    binary = binary_list_maker(n)
                flag = False
                binary[len(binary) - 1 - (n - 1)] = 1
                decimal -= 2 ** (n - 1)
                break
        if decimal == 0:
            break
    return binary

# Ex. C.1:
#def sc(a,b,c): 
    #return a*a*a+b*b*b+c*c*c
# There are three main style mistakes: the title of the function is not
# meaningful, there are no spaces inbetween the variables and operators, and
# there are not spaces after commas
def sum_of_cubes(a, b, c): 
    return a * a * a + b * b * b + c * c * c


# Ex. C.2:
#def sumofcubes(argumenta, argumentb, argumentc, argumentd):
    #retrn sumof cubes of argsa b c &d
    #return argumenta * argumenta * argumenta + argumentb * argumentb * argumentb + argumentc * argumentc * argumentc + argumentd * argumentd * argumentd
# There are four style mistakes: The name and arguments do not illustrate the
# boundaries of words, the arguments have too long of names, the comment has
# grammar and spelling mistakes, the math could be written more clearly using
# exponents, and one line is longer than 80 characters, and the arguments in 
# the comment do not match the arguments in the function, and there should also
# be a space after the octothorpe.
def sum_of_cubes(a, b, c, d):
    # return sum of cubes of args a, b, c, and d
    return (a ** 3) + (b ** 3) + (c ** 3) + (d ** 3)

# Ex. C.3:
# 2 different kinds of style mistakes:
def sum_of_squares(x, y):
         return x * x + y * y
def sum_of_three_cubes(x, y, z):
    return x * x * x + y * y * y + z * z * z
# There should be parentheses around operations that take precedence over
# others, the math in the second function could be written more clearly using
# exponents, the indentation is inconsistent and there should be a blank line
# inbetween functions:

# 2 different kinds of style mistakes:
def sum_of_squares(x, y):
    return (x * x) + (y * y)
   
def sum_of_three_cubes(x, y, z):
    return (x ** 3) + (y ** 3) + (z ** 3)
