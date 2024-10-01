from pathlib import Path

from problem import Problem


def check_argument(args: list, problem: Problem):
    prog_name = Path(__file__).name
    if len(args) == 0:
        print(f"Usage: python3 {prog_name} (1|2)")
        exit(0)

    if not problem.routine_exists(args[0]):
        print(f"No registered method: {args[0]}")
        exit(0)
