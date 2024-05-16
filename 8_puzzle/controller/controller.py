import re
from model.puzzle import Puzzle
from model.search import Search
from timeit import default_timer as timer


class Controller:
    def __init__(self, view):
        self.new_puzzle = None
        self.view = view

    '''get and validate inputs'''
    def get_inputs(self):
        puzzle, answer = self.view.get_user_input()
        puzzle = puzzle.strip()
        answer = answer.strip()

        # Check inputs
        pattern = r"^[0-8]{9}$"
        comp = re.compile(pattern)
        check1 = comp.match(puzzle)
        check2 = comp.match(answer)
        while not check1 and not check2:
            check1 = comp.match(puzzle)
            check2 = comp.match(answer)
            puzzle, answer = self.view.get_user_input()

        # making new puzzle
        self.make_puzzle(puzzle, answer)

        # Get the search method
        search_method = self.view.choose_search_method()

        # search and print results
        self.search(search_method)

    '''Makes a new puzzle'''
    def make_puzzle(self, puzzle, answer):
        puzzle_list = []
        answer_list = []
        self.new_puzzle = Puzzle(3)
        for number in puzzle:
            puzzle_list.append(number)
        for number in answer:
            answer_list.append(number)
        self.new_puzzle.read_puzzle(puzzle_list, answer_list)

    '''Search for answer, time the process and print results'''
    def search(self, method):

        s = Search(self.new_puzzle)
        # IDS
        if method == '2':
            start = timer()
            result, count = s.iterative_deepening()
            end = timer()
        # A*
        else:
            heuristic_no = self.view.choose_heuristic()
            start = timer()
            result, count = s.a_search(heuristic_no)
            end = timer()

        self.view.print_results(start, end, self.new_puzzle, result, count)
