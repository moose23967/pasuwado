from qsharp import Result as QsharpResult
from qsharp import eval as qsharp_eval


class Randomizer:
    def __init__(self):
        with open("pasuwado/Randomizer.qs") as main:
            qsharp_eval(main.read())

    def generate_random_int_in_range(self, max: int) -> int:
        return qsharp_eval(f"Randomizer.GenerateRandomIntInRange({max})")

    def generate_random_result(self) -> QsharpResult:
        return qsharp_eval("Randomizer.GenerateRandomResult()")
