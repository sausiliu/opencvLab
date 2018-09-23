from __future__ import print_function

class BlockColors:
    BLUE = '\033[44m'
    GREEN = '\033[42m'
    YELLOW = '\033[103m'
    RED = '\033[41m'
    WHITE = '\033[47m'
    ORANGE = '\033[105m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLOCK = ' '*2
    SPACE = ' '*2

'''
bc = BlockColors()
print(bc.BLUE, end=bc.BLOCK)
print(bc.END, end=bc.SPACE)
print(bc.RED, end=bc.BLOCK)
print(bc.END, end=bc.SPACE)
print(bc.RED, end=bc.BLOCK)
print(bc.END)
print(bc.RED, end=' ')
print(bc.RED, end=' ')
'''

class Printer(object):
    def __init__(self, cube, isColour=True):
        self.cube = cube
        self.isColour = isColour
        self.bc = BlockColors()
        self.size = cube.size

    def print_up_down(self, face):
        space_len = self.cube.size * 2
        for row in range(self.size):
            print(self.bc.SPACE * space_len, end='')
            for column in range(self.size):
                if (column % 2) != 0:
                    print('|', end='')
                    self.print_colour(self.cube.faces[face].get_colour(row, column))
                    print('|', end='')
                else:
                    self.print_colour(self.cube.faces[face].get_colour(row, column))
            print()
            if row != self.size - 1:
                print(self.bc.SPACE * space_len + '---|---|---')

    def print_LFRB(self):
        for row in range(self.size):
            for face in ['L', 'F', 'R', 'B']:
                for column in range(self.size):
                    if (column % 2) != 0:
                        print('|', end='')
                        self.print_colour(self.cube.faces[face].get_colour(row, column))
                        print('|', end='')
                    else:
                        self.print_colour(self.cube.faces[face].get_colour(row, column))
                if face != 'B':
                    print('|', end='')
            print()
            if row != self.size - 1:
                print('---|---|---|---|---|---|---|---|---|---|---|---')

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

            print('', self.bc.END, end='')
        else:
            print()
    def print_cube(self):
        self.print_up_down('U')
        print('            ---|---|---')
        self.print_LFRB()
        print('            ---|---|---')
        self.print_up_down('D')

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

printCube.print_cube()

#print(cube.faces['U'].get_colour(0, 0))
