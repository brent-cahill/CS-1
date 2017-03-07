'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        self.board = []
        for i in range(9):
            self.board.append([])
        self.moveList = []

    def load(self, filename):
        count = 0
        fle = open(filename,'r')
        for i in fle:
            for j in range(len(i)):
                if i[j] != '\n' and i[j] != '':
                    self.board[count].append(int(i[j]))
            count += 1
        fle.close()

    def save(self, filename):
        fyle = open(filename, 'w')
        for i in self.board:
            for j in self.board[i]:
                fyle.write(self.board[i[j]])
            fyle.write('\n')

    def show(self):
        '''Pretty-print the current board representation.'''
        print
        print '   1 2 3 4 5 6 7 8 9 '
        for i in range(9):
            if i % 3 == 0:
                print '  +-----+-----+-----+'
            sys.stdout.write('%d |' % (i + 1))
            for j in range(9):
                if self.board[i][j] == 0:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('%d' % self.board[i][j])
                if j % 3 != 2 :
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('|')
            print 
        print '  +-----+-----+-----+'
        print

    def move(self, row, col, val):
        if val < 0 or val > 9:
            raise SudokuMoveError('Value is not an accepted number')
        
        if self.board[col][row] != 0 and val !=0:
            raise SudokuMoveError('Space is occupied')        
        
        if val in self.board[col] and val !=0:
            raise SudokuMoveError('Row conflict')
            
        for i in self.board:
            if val == i[row] and val !=0:
                raise SudokuMoveError('Column Error')
            
        self.board[col][row] = val
        self.moveList.append((row, col, val))

    def undo(self):
        if self.moveList != []:
            tup = self.moveList.pop()
            self.move(tup[0], tup[1], 0)

    def solve(self):
        while True:
            inp = raw_input('Sudoku> ')
            if inp == 'q':
                break
            elif inp == 'u':
                self.undo()
            elif inp[0] == 's':
                try:
                    self.save(inp[2:])
                except TypeError:
                    raise SudokuCommandError('Not an accepted Sudoku move')                
            elif len(inp) == 3:
                try:
                    self.move(int(inp[1]) - 1, int(inp[0]) - 1, int(inp[2]))
                except ValueError:
                    raise SudokuCommandError('Not an accepted Sudoku move')
            else:
                raise SudokuCommandError('Not an accepted Sudoku move')
            s.show()
            for i in self.board:
                if 0 not in i:
                    done = True
                if 0 in i:
                    done = False
                    print "Congratulations! You've solved the puzzle!"
                    break
            if done == True:
                break
                

if __name__ == '__main__':
    s = Sudoku()
    
    while True:
        filename = raw_input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError, e:
            print e

    s.show()
    try:
        s.solve()
    except SudokuError,e:
        print e
        s.show()
        s.solve()
    except SudokuCommandError, e:
        print e
        s.show()
        s.solve()
    except SudokuMoveError, e:
        print e
        s.show()
        s.solve()
