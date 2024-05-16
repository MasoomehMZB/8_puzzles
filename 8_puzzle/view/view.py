class View:
    @staticmethod
    def get_user_input():
        puzzle = input("Puzzle: ")
        answer = input("Answer: ")
        return puzzle, answer

    @staticmethod
    def choose_search_method():
        print("Choose search method:\n[1] A*\n[2] IDS")
        search_method = input()
        return search_method


    @staticmethod
    def choose_heuristic():
        choice = input("Choose heuristic(from 1 to 3):")
        return choice

    @staticmethod
    def print_results(start, end, new_puzzle, result, count):
        result.print_sequence(new_puzzle)
        print("Moves:", result.moves)
        print("Number of visited nodes:", count)
        print(f"Time: {round(end - start, 3)}s")
