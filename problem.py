class Problem:
    def __init__(self) -> None:
        self.__routine = dict()

    def register(self, routine_name: str, routine: object) -> None:
        self.__routine[routine_name] = routine

    def get_routine_name(self, routine_name: str) -> str:
        if not routine_name:
            return ""
        return self.__routine[routine_name].__name__

    def routine_exists(self, routine_name: str) -> bool:
        if not routine_name:
            return False
        return routine_name in self.__routine.keys()

    def run(self, routine_name: str, data: list) -> None:
        routine = self.__routine[routine_name]
        if not routine:
            print(f"No command: {routine_name}")
            exit(1)
        if not data or len(data) == 0:
            print("Invalid input")
            exit(2)
        routine(data)
