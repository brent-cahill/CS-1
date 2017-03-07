import random
def make_random_code():
    """
    Generates a string of 4 random letters from the choices R, G, B, Y, O, and
    W.
    """
    colors = ['R', 'G', 'B', 'Y', 'O', 'W']
    stringColors = ''
    for x in range(4):
        stringColors += random.choice(colors)
    return stringColors

def count_exact_matches(str1, str2):
    """
    Counts the number of exact (same letter, same place) matches of two strings.
    
    Arguments: str1 and str2, the two strings to be compared
    
    Output: the number (int) of exact matches.
    """
    checkCount1 = 0
    for y in range(4):
        if str1[y] == str2[y]:
            checkCount1 += 1
    return checkCount1

def count_letter_matches(str3, str4):
    """
    Counts the number of letter matches (same letter, same or different place)
    of two strings.
    
    Arguments: str3 and str4, the two strings to be compared
    
    Output: the number (int) of letter matches.
    """
    str3 = list(str3)
    str4 = list(str4)
    checkCount2 = 0
    for y in str3:
        if y in str4:
            checkCount2 += 1
            str4.remove(y)
    return checkCount2

def compare_codes(code, guess):
    """
    Compares the two strings for both letter matches and exact matches, calling
    upon the count_exact_matches and count_letter_matches functions. A letter
    match but not an exact match will be prepresented as a 'w' in the output
    string, while an exact match will be represented by a 'b'. A '-' will be
    outputted for any letters that are neither letter nor exact matches.
    
    Arguments: code and guess, the two strings to be compared
    
    Output: a string consisting of 'w's, 'b's, and '-'s that represent how many
    letters were letter, exact and no matches, respectively.
    """
    numBlack = count_exact_matches(code, guess)
    numWhite = count_letter_matches(code, guess) - numBlack
    numBlank = 4 - (numBlack + numWhite)
    return 'b' * numBlack + 'w' * numWhite + '-' * numBlank
    

def run_game():
    """
    Runs the game "mastermind." Calls upon the make_random_code function to
    create a 4 letter string (code), then asks the user for input of another 4
    letter string (guess) which it compares to the random 4 letter string using
    the compare_codes function, and prints out the resulting string which
    represents how close the guess is to the code. Repeats until the guess is
    the same as the code.
    """
    print 'New game.'
    mastercode = make_random_code()
    counter = 0
    while True:
        guesscode = raw_input('Enter your guess: ')
        counter += 1
        comp = compare_codes(mastercode, guesscode)
        print "Result: %s" %comp
        if comp == 'bbbb':
            print "Congratulations! You cracked the code in %d moves!" %counter
            break