from qsharp import eval as qsharp_eval


class RandomNumberGenerator:
    def __init__(self):
        with open("pasuwado/modules/RandomNumberGenerator.qs") as main:
            qsharp_eval(main.read())

    def generate(self, max: int) -> int:
        return qsharp_eval(f"RandomNumberGenerator.Generate({max})")
