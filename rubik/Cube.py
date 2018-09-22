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
            print(self.bc.BLOCK * self.cube.size, end='') #
            for column in range(self.size):
                if (column % 2) != 0:
                    print('|', end='')
                    self.print_colour(self.cube.faces['U'].get_colour(row, column))
                    print('|', end='')
                else:
                    self.print_colour(self.cube.faces['U'].get_colour(row, column))
            print()
            if row != self.size - 1:
                print('       -   -   -')

    def print_colour(self, colour):
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

            print('', self.bc.ENDC, end='')
        else:
            print()

class Face(object):
    COLOURS = ['r', 'g', 'b', 'w', 'y', 'o']
    def __init__(self, size=3):
        self.size = size
        self.square_size = size * size
        self.view = ' ' * self.square_size

    def set_colours(self, colours):
        if len(colours) != self.square_size:
            raise ValueError('Invalid colours')
        for c in colours:
            if c not in self.COLOURS:
                raise ValueError('Invalid colour')
        self.view = colours
        return self

    def set_colour(self, row, column, colour):
        if c not in self.COLOURS:
            raise ValueError('Invalid colour')
        self.view = self.view[:(row * self.size + column)] + \
                    colour + \
                    self.view[:(row * self.size + column + 1)]
        return self

    def get_colour(self, row, column):
        return self.view[row * self.size + column]

class Cube(object):
    FACES = ['U', 'L', 'F', 'R', 'B', 'D']
    def __init__(self, size):
        self.size = size
        self.faces = {
            'U' : Face(self.size),
            'L' : Face(self.size),
            'F' : Face(self.size),
            'R' : Face(self.size),
            'B' : Face(self.size),
            'D' : Face(self.size)
        }
        square_size = size * size
        self.faces['U'].set_colours('r' * square_size)
        self.faces['L'].set_colours('g' * square_size)
        self.faces['F'].set_colours('b' * square_size)
        self.faces['R'].set_colours('w' * square_size)
        self.faces['B'].set_colours('y' * square_size)
        self.faces['D'].set_colours('o' * square_size)

cube = Cube(3)
printCube = Printer(cube)

printCube.print_up()

#print(cube.faces['U'].get_colour(0, 0))
