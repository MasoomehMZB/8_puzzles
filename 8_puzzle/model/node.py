from queue import Queue
from copy import deepcopy, copy

heuristic = 0


class Node:
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle
        self.parent = parent
        if parent is None:
            self.depth = 0
            self.moves = move
        else:
            self.depth = parent.depth + 1
            self.moves = parent.moves + move

    def __lt__(self, other):
        # Define comparison based on heuristic value and depth
        return (self.choose_heuristic(heuristic) + self.depth) < (other.choose_heuristic(heuristic) + other.depth)

    '''heuristic 1'''
    def heuristic1(self):
        result = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.state.puzzle[i][j] != self.state.solved[i][j]
                        & self.state.puzzle[i][j] != self.state.zero):
                    result += 1
        return result

    '''heuristic 2'''
    def heuristic2(self):
        result = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.state.puzzle[i][j] != self.state.solved[i][j]
                        & self.state.puzzle[i][j] != self.state.zero):
                    i2 = self.state.solved_dict.get(self.state.puzzle[i][j])[0]
                    j2 = self.state.solved_dict.get(self.state.puzzle[i][j])[1]
                    result += abs(i - i2) + abs(j - j2)

        return result

    '''heuristic 3 : number of misplaced tiles + number of tiles that are in both wrong rows and columns'''
    def heuristic3(self):

        wrong_row_column = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.state.puzzle[i][j] != self.state.solved[i][j] &
                        self.state.puzzle[i][j] != self.state.zero):

                    i2 = self.state.solved_dict.get(self.state.puzzle[i][j])[0]
                    j2 = self.state.solved_dict.get(self.state.puzzle[i][j])[1]
                    if i2 != i & j2 != j:
                        wrong_row_column += 1

        result = wrong_row_column + self.heuristic1()
        return result

    '''choose the wanted heuristic'''
    def choose_heuristic(self, choice):
        global heuristic
        heuristic = choice
        if choice == '1':
            heuristic_value = self.heuristic1()
        elif choice == '2':
            heuristic_value = self.heuristic2()
        else:
            heuristic_value = self.heuristic3()

        return heuristic_value


    # '''heuristic 3 : works for puzzles bigger than 3x3
    # otherwise no different from manhattan'''
    # def heuristic3(self):
    #
    #     result = 0
    #     wrong_row = 0
    #     wrong_column = 0
    #     for i in range(0, 3):
    #         for j in range(0, 3):
    #             if (self.state.puzzle[i][j] != self.state.solved[i][j] &
    #                     self.state.puzzle[i][j] != self.state.zero):
    #
    #                 i2 = self.state.solved_dict.get(self.state.puzzle[i][j])[0]
    #                 j2 = self.state.solved_dict.get(self.state.puzzle[i][j])[1]
    #                 if i2 != i:
    #                     wrong_row += 1
    #                 if j2 != j:
    #                     wrong_column += 1
    #
    #     result = wrong_row + wrong_column + self.heuristic1()
    #     return result

    '''Checks if the Node's state is a goal state'''
    def goal_state(self):
        return self.state.check_puzzle()

    '''Generates the node's children states'''
    def succ(self):
        succ = Queue()
        for move in self.state.moves:
            puzzle = deepcopy(self.state)
            puzzle.move_toward(move)
            if puzzle.zero is not self.state.zero:
                succ.put(Node(puzzle, self, move))

        return succ

    '''Prints the answer'''
    def print_sequence(self, puzzle):
        puzzle.print_puzzle()

        print("\n-------------\n")
        for move in self.moves:
            puzzle.move_toward(move)
            puzzle.print_puzzle()
            print("\n-------------\n")






