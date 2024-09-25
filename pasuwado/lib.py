from qsharp import eval as qsharp_eval
from qsharp import Result as QsharpResult


class Pasuwado:
    def __init__(self) -> None:
        with open("pasuwado/Lib.qs") as main:
            qsharp_eval(main.read())

    def generate_random_int_in_range(self, max: int) -> int:
        return qsharp_eval(f"Pasuwado.GenerateRandomIntInRange({max})")

    def generate_random_result(self) -> QsharpResult:
        return qsharp_eval("Pasuwado.GenerateRandomResult()")


class Generator:
    def __init__(self, pasuwado: Pasuwado) -> None:
        self.pasuwado = pasuwado

    def generate(self, size: int) -> str:
        characters = [chr(i) for i in range(33, 127)]

        return "".join(
            [
                characters[self.pasuwado.generate_random_int_in_range(len(characters) - 1)]
                for _ in range(size)
            ]
        )
