import random
import itertools
import collections
import time
import importlib
import ray
import pathlib
import os
# from Algorithm import A_star, BFS, DFS
# from Problem import Puzzle

# board = [[1,2,3],[4,5,0],[6,7,8]]
# puzzle = Puzzle(board)
# #puzzle = puzzle.shuffle()
# # s = A_star(puzzle)
# s = BFS(puzzle)
# tic = time.time()
# p = s.solve()
# toc = time.time()

# steps = 0
# for node in p:
#     print(node.action)
#     node.puzzle.pprint()
#     steps += 1

# print("Total number of steps: " + str(steps))
# print("Total amount of time in search: " + str(toc - tic) + " second(s)")


class RunningAlgorithm:
    def __init__(self, algorithm_name, problem_name) -> None:
        try:
            algorithm_module = importlib.import_module(
                "Algorithm."+algorithm_name)
            problem_moule = importlib.import_module("Problem." + problem_name)
            self.Algorithm = algorithm_module.Solve
            self.Problem = problem_moule.Puzzle

        except ModuleNotFoundError as err:
            print(
                f"{algorithm_name} or {problem_moule} are not a supported in this test"
            )
            raise err

    def solve(self):
        puzzle = self.Problem()
        # puzzle = puzzle.shuffle()
        # s = A_star(puzzle)
        s = self.Algorithm(puzzle)
        tic = time.time()
        p = s.solve()
        toc = time.time()

        steps = 0
        for node in p:
            print(node.action)
            node.puzzle.pprint()
            steps += 1

        print("Total number of steps: " + str(steps))
        print("Total amount of time in search: " +
              str(toc - tic) + " second(s)")

    def load_init_algorithm(self):
        print("\nWATTING IN MY NEXT VERSION. LOL")
        pass

    def load_init_problem(self):
        print("\nWATTING IN MY NEXT VERSION. LOL")
        pass

    def evaluate(self):
        print("\nWATTING IN MY NEXT VERSION. LOL")
        pass


if __name__ == "__main__":
    while True:
        os.system('clear')
        print("\nWelcome to Introduction AI! Here's a list of algorithm: ")
        # Choice Algorithm
        algorithms = [
            filename.stem
            for filename in sorted(list((pathlib.Path.cwd()/"Algorithm").glob("*.py")))
            # if filename.name != "..."
        ]

        for i in range(len(algorithms)):
            print(f"{i}. {algorithms[i]}")
        choice = input("Enter a number to choose the algorithm: ")
        valid_input = [str(i) for i in range(len(algorithms))]
        while choice not in valid_input:
            choice = input("invalid input, enter a number listed above: ")
        # Initialize Algorithm
        choice = int(choice)
        algorithm_name = algorithms[choice]

        # Choice Problem
        problems = [
            filename.stem
            for filename in sorted(list((pathlib.Path.cwd()/"Problem").glob("*.py")))
            # if filename.name != "..."
        ]

        print("\n---------------------------------")
        for i in range(len(problems)):
            print(f"{i}. {problems[i]}")
        choice = input("Enter a number to choose the problem: ")
        valid_input = [str(i) for i in range(len(problems))]
        while choice not in valid_input:
            choice = input("invalid input, enter a number listed above: ")
        # Initialize Algorithm
        choice = int(choice)
        problem_name = problems[choice]

        running_algorithm = RunningAlgorithm(algorithm_name, problem_name)

        while True:
            # Configure running options
            options = [
                "Solve",
                "Load Initialize Algorithm ",
                "Load Initialize Problem",
                "Evaluate",
                "Trying something else",
                "Exit"
            ]
            running_out = False
            print("\n---------------------------------")
            print("Choose your action")
            for i in range(len(options)):
                print(f"{i}. {options[i]}")
            choice = input("Enter a number to choose an actions: ")
            valid_input = [str(i) for i in range(len(options))]
            while choice not in valid_input:
                choice = input("Invalid input, enter a number listed above: ")
            choice = int(choice)

            if choice == 0:
                running_algorithm.solve()
                pass
            elif choice == 1:
                running_algorithm.load_init_algorithm()
                pass
            elif choice == 2:
                running_algorithm.load_init_problem()
                pass
            elif choice == 3:
                running_algorithm.evaluate()
                pass
            elif choice == 4:
                break
            else:
                del running_algorithm
                running_out = True
                break

            print("\nDone")
        ray.shutdown()

        if running_out == True:
            break
