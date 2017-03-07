import random
def random_size(a, b):
    """
    Takes 2 nonnegative even integers 'a' and 'b', where a < b, and returns
    a random even int >= a and <= b.
    """
    assert a >= 0 and b >= 0, 'inputs positive'
    assert a % 2 == 0 and b % 2 == 0, 'inputs even'
    assert a < b, 'first input smaller'
    rand = 2 * random.randint(a / 2, b / 2)
    assert rand % 2 == 0, 'output even'
    return rand

def random_position(max_x, max_y):
    """
    Takes 2 nonnegative integers 'max_x' and 'max_y' and returns a random tuple
    within those bounds
    """
    assert max_x >= 0 and max_y >= 0
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    return (x, y)

def random_color():
    """
    Returns a random hexadecimal color
    """
    color = '#'
    for i in range(6):
        color += random.choice('0123456789abcdef')
    return color

def count_values(dic):
    """
    Counts the number of distinct values of a dictionary 'dic'
    """
    values = dic.values()
    check = []
    count = 0
    for i in values:
        if i not in check:
                count += 1
                check.append(i)
    return count

def remove_value(dic, val):
    """
    removes all of the instances of a single value 'val' from a dictionary 'dic'
    """
    dels = []
    for i in dic:
        if dic[i] == val:
            dels.append(i)   
    for i in dels:
        del dic[i]

def split_dict(dic):
    """
    Splits a dictionary 'dic' into two distinct dictionaries d1 and d2 based on
    the key's first letter: d1 if the key is from 'a' to 'm', d2 if the key is
    from 'n' to 'z', then returns a tuple of d1 and d2. Keys starting with non-
    letters are not included in either dict.
    """
    d1 = {}
    d2 = {}
    for i in dic:
        letter = i[0]
        if letter.upper() <= 'M' and letter.upper() >= 'A':
            d1[i] = dic[i]
        if letter.upper() > 'M' and letter.upper() <= 'Z':
            d2[i] = dic[i]
    return (d1, d2)

def count_duplicates(dic):
    """
    Counts the number of duplicate values in dic, then returns the count
    """
    values = dic.values()
    count = 0
    counted = []
    for i in values:
        if values.count(i) > 1:
            counted.append(i)
            if counted.count(i) <= 1:
                count += 1
    return count        