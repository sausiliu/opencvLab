class BlockColors:
    BLUE = '\033[44m'
    GREEN = '\033[102m'
    YELLOW = '\033[103m'
    RED = '\033[101m'
    WHITE = '\033[107m'
    ORANGE = '\033[48;5;214m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Printer(object):
    def __init__(self, cube):
        self._cube = cube

    @property
    def cube(self):
        return self._cube.to_native_cube()

    def pprint(self):
        pass


class TtyPrinter(Printer):
    def __init__(self, cube, colours=True):
        self.colours = colours
        super(TtyPrinter, self).__init__(cube)

    def pprint(self):
        self.print_upper()
        self.print_center()
        self.print_down()

    def print_upper(self):
        for i in range(self.cube.size * 2 + 1):
            print(' ' * (self.cube.size * 6), end=' ')
            if (i % 2) == 0:
                for j in range(self.cube.size * 2):
                    if (j % 2) == 0:
                        print('|', end=' ')
                    else:
                        print('---', end=' ')
                print('|')
            else:
                for j in range(self.cube.size * 2):
                    if (j % 2) == 0:
                        print('|', end=' ')
                    else:
                        self.print_square(self.cube.faces['U'].get_colour(int(i / 2), int(j / 2)))
                print('|')

    def print_center(self):
        for i in range(self.cube.size * 2 + 1):
            for face in ['L', 'F', 'R', 'B']:
                if (i % 2) == 0:
                    for j in range(self.cube.size * 2):
                        if (j % 2) == 0:
                            print('|', end=' ')
                        else:
                            print('---', end=' ')
                else:
                    for j in range(self.cube.size * 2):
                        if (j % 2) == 0:
                            print('|', end=' ')
                        else:
                            self.print_square(self.cube.faces[face].get_colour(int(i / 2), int(j / 2)))
                print('|', end=' ')
            print()

    def print_down(self):
        for i in range(self.cube.size * 2 + 1):
            print(' ' * (self.cube.size * 6), end=' ')
            if (i % 2) == 0:
                for j in range(self.cube.size * 2):
                    if (j % 2) == 0:
                        print('|', end=' ')
                    else:
                        print('---', end=' ')
                print('|')
            else:
                for j in range(self.cube.size * 2):
                    if (j % 2) == 0:
                        print('|', end=' ')
                    else:
                        self.print_square(self.cube.faces['D'].get_colour(int(i / 2), int(j / 2)))
                print('|')

    def print_square(self, c):
        if self.colours:
            if c == 'w':
                print(BlockColors.WHITE, end=' ')
            elif c == 'b':
                print(BlockColors.BLUE, end=' ')
            elif c == 'g':
                print(BlockColors.GREEN, end=' ')
            elif c == 'r':
                print(BlockColors.RED, end=' ')
            elif c == 'y':
                print(BlockColors.YELLOW, end=' ')
            elif c == 'o':
                print(BlockColors.ORANGE, end=' ')
            print(' ', BlockColors.END, end=' ')
        else:
            print(c.upper(), end=' ')
