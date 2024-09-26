from qsharp import Result as QsharpResult
from qsharp import eval as qsharp_eval


class RandomNumberGenerator:
    def __init__(self):
        with open("pasuwado/RandomNumberGenerator.qs") as main:
            qsharp_eval(main.read())

    def generate_random_int_in_range(self, max: int) -> int:
        return qsharp_eval(f"RandomNumberGenerator.GenerateRandomIntInRange({max})")

    def generate_random_result(self) -> QsharpResult:
        return qsharp_eval("RandomNumberGenerator.GenerateRandomResult()")
