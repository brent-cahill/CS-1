# Name: Brent Cahill
# CMS cluster login name: bcahill

import random
import sys
import string

# Problem 1.1:
# The syntax errors here are: the elif statement 'elif item = n:' should read as
# 'elif item == n:', a single equals sign is used as a variable assignment
# operator, while a double equals sign is used as a relational operator.
# Another error is that the if and elif statements have inconsistent indentation
# A third error is that the return statement won't work. In order to return a
# tuple, the things to be returned must be seperated by commas. The 4th error
# can be seen in the for loop line: The for loop ends with a semicolon instead
# of a colon, which is a syntax error. The last error comes in the "docstring,"
# which, as of right now is simply a string. In order to make a docstring, you
# must use three quotes to seperate it from the rest of the function.

# Promblem 1.2:
# The symantic errors here are: The 'n -= 1' statement should be within the
# while loop in the function 'factorial'. Another error comes where n =
# int(raw_input). To work with the second function, n should be an argument for
# the function. In the function 'sin,' n should also start at 1, not 3, so the
# line should read as 'n = 1'. The line in which tiny is assigned a value should
# also use a single equals sign rather than the relational operator '=='.
# Lastly, the function 'sin' calls on 'factorial' using an argument, but
# factorial takes no arguments, as stated above.

# Problem 1.3:
# The style errors here are: 1. The title is not meaningful 2. The docstring is
# written inside quotes, not after triple quotes 3. The comments also have
# incorrect grammar and spelling 4. There should always be a space before and
# after an operator, like the assignment operator '=': ie. 'b = []' 5. The
# indention is inconsistent throughout the function. 6. There is no need for an
# else statement with a pass statement within it. 7. Similarly to 4, there
# should be a space before and after mathematical operators like '+' and '+='.

# Problem 2.1
def random_walk(n, m):
    """
    Simulates a 'random walk' by a point in one-dimension. Takes two integer
    arguments n and m, which represent a threshold to be achieved in the random
    walk, and the number of times for the simulation to be repeated,
    respectively. Returns the average number of 'steps' taken to reach the
    threshold after m simulations.
    """
    results = []
    for i in range(m):
        pos = 0
        step = 0.0
        while abs(pos) < n:
            step += 1
            pos += random.choice([1, -1])
        results.append(step)
    return sum(results) / m
### the value is usually approximately equal to n ** 2

# Problem 2.2:
def draw_box(n, p):
    """
    Uses the sys module to write a box of size n x n (where n is a positive
    integer) containing 'O's and ' 's with a probability p of finding a 'O'
    at a given space.
    """
    assert n > 0
    assert p <= 1.0 and p >= 0.0
    write = sys.stdout.write
    write('+' + '-' * n + '+' + '\n')
    for i in range(n):
        write('|')
        for i in range(n):
            if random.random() < p:
                write('O')
            else:
                write(' ')
        write('|')
        write('\n')
    write('+' + '-' * n + '+')

# Problem 2.3:
def initial_value_count(lst):
    """
    Returns a tuple of: the first element of list 'lst', and the number of
    subsequent times that element is repeated in a row immediately following
    the first element.
    """
    assert len(lst) > 0
    count = 0
    for i in lst:
        if i == lst[0]:
            count += 1
        else:
            break
    return (lst[0], count)

def run_length_encode(lst):
    """
    Uses the initial_value_count function to represent the elements of a list 
    lst as a list of tuples with the values of each element and the number of
    subsequent identical elements. Also known as "run-length encoding"
    """
    lst2 = []
    while len(lst) > 0:
        lst2.append(initial_value_count(lst))
        count = initial_value_count(lst)[1]
        lst[0:count] = []
    return lst2

# Problem 3.1:
def make_subst_dicts():
    """
    Generates a dictionary which maps out the lowercase alphabet to random
    other members of the alphabet, in a one to one method (ie, each letter has a
    unique other letter it is mapped to).
    """
    key = []
    val = []
    key [:0] = string.lowercase
    val [:0] = string.lowercase
    en = {}
    de = {}
    for i in range(26):
        a = random.choice(key)
        b = random.choice(val)
        en [a] = b
        de [b] = a
        key.remove(a)
        val.remove(b)
    return (en, de)

# Problem 3.2:        
def encode_subst(dic, phrase):
    """
    Replaces the words in a word or phrase 'phrase' with the letter map 'dic'
    which is a dictionary whihc maps out the alphabet as defined in the previous
    function.
    """
    strin = ''
    for i in phrase:
        if i in string.uppercase:
            strin += dic[i.lower()].upper()
        elif i in string.lowercase:
            strin += dic[i]
        else:
            strin += i
    return strin

# Problem 3.3:
def encode_seq(code, phrase):
    """
    Encodes or decodes -- depending on 'code' -- a phrase 'phrase' according to
    sequential code cryptography. The code is as follows: The first character is
    unchanged. Every subsequent character is assigned the letter value of (the
    numerical value of the previous encrypted character plus the numerical value
    of the character to be encrypted) modulo 26.
    """
    assert code == 'en' or code == 'de'
    strin = ''
    oldVal = 0
    if code == 'en':
        for i in phrase:
            if i in string.letters:
                newVal = (oldVal + ord(i.lower()) - ord('a')) % 26
                oldVal = newVal
                newChar = chr(newVal + ord('a'))                
                if i in string.lowercase:
                    strin += newChar
                elif i in string.uppercase:
                    strin += newChar.upper()
            else:
                strin += i
        return strin
    if code == 'de':
        for i in phrase:
            if i in string.letters:
                phraseVal = ord(i.lower()) - ord('a')
                newVal = (phraseVal - oldVal) % 26
                newChar = chr(newVal + ord('a'))           
                if i in string.lowercase:
                    strin += newChar
                elif i in string.uppercase:
                    strin += newChar.upper()
                oldVal = phraseVal  
            else:
                strin += i
        return strin
    
def encode(code, tup, phrase):
    """
    Combines the encryption of both substitution and sequential codes, as
    described in the two previous functions. The function first encrypts using
    encode_seq, then uses encode_subst.
    """
    assert code == 'en' or code == 'de'
    if code == 'en':
        halfEn = encode_seq('en', phrase)
        final = encode_subst(tup[0], halfEn)
    elif code == 'de':
        halfDe = encode_subst(tup[1], phrase)
        final = encode_seq('de', halfDe)
    return final

def encode_file(code, tup, fyle, newFyle):
    """
    Either encodes (code == 'en') or decodes (code == 'de') the contents of a
    file 'fyle' into another file 'newFyle' according to the function above.
    """
    assert code == 'en' or code == 'de'
    fle = open(fyle, 'r')
    fle2 = open(newFyle, 'w')
    while True:
        line = fle.readline()
        if line == '':
            break
        else:
            fle2.write(encode(code, tup, line))
    fle.close()
    fle2.close()    