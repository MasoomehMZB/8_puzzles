from queue import LifoQueue
from queue import PriorityQueue
from model.node import Node


class Search:

    '''Defining the start node'''
    def __init__(self, puzzle):
        self.start = Node(puzzle)

    '''IDS'''
    def iterative_deepening(self):
        depth = 0
        count = 0
        sum = 0
        result = None
        while result is None:
            result, count = self.depth_limited(depth)
            sum += count
            depth += 1
        return result, sum

    '''DFS'''
    def depth_limited(self, depth):
        leaves = LifoQueue()
        leaves.put(self.start)
        count = 0
        while True:
            if leaves.empty():
                return None, count
            current = leaves.get()
            count += 1
            if current.goal_state():
                return current, count
            elif current.depth is not depth:
                succ = current.succ()
                while not succ.empty():
                    leaves.put(succ.get())

    '''A*'''
    def a_search(self, heuristic_no):
        leaves = PriorityQueue()
        leaves.put((self.start.choose_heuristic(heuristic_no) + self.start.depth, self.start))
        closed = []
        while True:
            if leaves.empty():
                return None, len(closed)
            current = leaves.get()[1]
            if current.goal_state():
                return current, len(closed)
            elif current.state.puzzle not in closed:
                closed.append(current.state.puzzle)
                succ = current.succ()
                while not succ.empty():
                    child = succ.get()
                    leaves.put((child.choose_heuristic(heuristic_no) + child.depth, child))



