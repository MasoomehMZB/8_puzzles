
class Puzzle:

    def __init__(self, size):
        self.size = size
        self.puzzle = []
        self.solved = []
        self.zero = (0, 0)
        self.moves = ["D", "L", "U", "R"]
        self.solved_dict = {}

        '''Make 2 3x3 grids'''
        count = 1
        for i in range(0, size):
            self.puzzle.append([])
            self.solved.append([])
            for j in range(0, size):
                self.puzzle[i].append(count)
                self.solved[i].append(count)
                count += 1
        self.puzzle[size - 1][size - 1] = 0
        self.solved[size - 1][size - 1] = 0
        self.zero = (size - 1, size - 1)

    '''Making the puzzle and wanted result using provided input'''
    def read_puzzle(self, num, result_num):
        count = 0
        for i in range(0, self.size):
            for j in range(0, self.size):
                if int(num[count]) == 0:
                    self.zero = (i, j)
                    self.puzzle[i][j] = 0
                self.puzzle[i][j] = int(num[count])
                self.solved[i][j] = int(result_num[count])
                self.solved_dict[int(result_num[count])] = (i, j)
                count += 1

    '''Check if the puzzle is solved'''
    def check_puzzle(self):

        if self.puzzle != self.solved:
            return False

        return True

    '''Swapping the empty space with a tile'''
    def swap(self, x1, y1, x2, y2):
        empty_space = self.puzzle[x1][y1]
        self.puzzle[x1][y1] = self.puzzle[x2][y2]
        self.puzzle[x2][y2] = empty_space

    '''Moving up the empty space'''
    def up(self):
        if self.zero[0] != 0:
            self.swap(self.zero[0], self.zero[1], self.zero[0] - 1, self.zero[1])
            self.zero = (self.zero[0] - 1, self.zero[1])

    '''Moving up the empty space'''
    def down(self):
        if self.zero[0] != self.size - 1:
            self.swap(self.zero[0], self.zero[1], self.zero[0] + 1, self.zero[1])
            self.zero = (self.zero[0] + 1, self.zero[1])

    '''Moving the empty space to the right'''
    def right(self):
        if self.zero[1] != self.size - 1:
            self.swap(self.zero[0], self.zero[1], self.zero[0], self.zero[1] + 1)
            self.zero = (self.zero[0], self.zero[1] + 1)

    '''Moving the empty space to the left'''
    def left(self):
        if self.zero[1] != 0:
            self.swap(self.zero[0], self.zero[1], self.zero[0], self.zero[1] - 1)
            self.zero = (self.zero[0], self.zero[1] - 1)

    '''Print the puzzle'''
    def print_puzzle(self):
        for i in range(0, self.size):
            print(self.puzzle[i])

    '''Making a move'''
    def move_toward(self, move):
        if move == "U":
            self.up()
        if move == "D":
            self.down()
        if move == "L":
            self.left()
        if move == "R":
            self.right()

