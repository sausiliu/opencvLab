import Cube

class BlockColors:
    BLUE = '\033[44m'
    GREEN = '\033[102m'
    YELLOW = '\033[103m'
    RED = '\033[101m'
    WHITE = '\033[107m'
    ORANGE = '\033[48;5;214m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLOCK = ' '*2
    SPACE = '|'

'''
bc = BlockColors()
print(bc.BLUE, end=bc.BLOCK)
print(bc.ENDC, end=bc.SPACE)
print(bc.RED, end=bc.BLOCK)
print(bc.ENDC, end=bc.SPACE)
print(bc.RED, end=bc.BLOCK)
print(bc.ENDC)
print(bc.RED, end=' ')
print(bc.RED, end=' ')
'''

class Printer(object):
    def __init__(self, cube, isColour=True):
        self.cube = cube
        self.isColour = isColour
        self.bc = BlockColors()
        self.size = cube.size

    def print_up(self):
        for row in range(self.size):
            print(self.bc.BLOCK * self.cube.size) #
            for column in range(self.size):
                self.print_cube(self.cube.faces['U'])

    def print_cube(self, colour):
        if self.isColour:
           if colour == 'r':
               print(self.bc.RED, end=self.bc.BLOCK)
           elif colour == 'g':
               print(self.bc.GREEN, end=self.bc.BLOCK)
           elif colour == 'b':
               print(self.bc.BLUE, end=self.bc.BLOCK)
           elif colour == 'w':
               print(self.bc.WHITE, end=self.bc.BLOCK)
           elif colour == 'y':
               print(self.bc.YELLOW, end=self.bc.BLOCK)
           elif colour == 'o':
               print(self.bc.ORANGE, end=self.bc.BLOCK)
        else:
            print()




