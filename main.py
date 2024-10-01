import sys

from functions import my_max, my_min, my_sum
from problem import Problem
from util import check_argument

PROG_NAME = "abc"


def main():
    problem = Problem()
    problem.register("1", my_max)
    problem.register("2", my_min)
    problem.register("3", my_sum)

    args = sys.argv[1:]
    check_argument(PROG_NAME, args, problem)
    command = args[0]
    print(f"Running: {problem.get_routine_name(command)}")
    data = [int(x) for x in input("Enter integers: ").split()]

    problem.run(command, data)


if __name__ == "__main__":
    main()
