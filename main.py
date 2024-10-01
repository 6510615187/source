import sys
from pathlib import Path

from problem import Problem

PROG_NAME = "abc"


def check_argument(args: list, problem: Problem) -> None:
    prog_name = Path(__file__).name
    if len(args) == 0:
        print(f"Usage: python3 {prog_name} (1|2)")
        exit(0)

    if not problem.routine_exists(args[0]):
        print(f"No registered method: {args[0]}")
        exit(0)


def my_max(data: list) -> None:
    current_max = data[0]
    for item in data:
        if item > current_max:
            current_max = item
    print(f"Data: {data}")
    print(f"Maximum: {current_max}")


def my_min(data: list) -> None:
    current_min = data[0]
    for item in data:
        if item < current_min:
            current_min = item
    print(f"Data: {data}")
    print(f"Minimum: {current_min}")


def main():
    problem = Problem()
    problem.register("1", my_max)
    problem.register("2", my_min)

    args = sys.argv[1:]
    check_argument(args, problem)
    command = args[0]
    print(f"Running: {problem.get_routine_name(command)}")
    data = [int(x) for x in input("Enter integers: ").split()]

    problem.run(command, data)


if __name__ == "__main__":
    main()
