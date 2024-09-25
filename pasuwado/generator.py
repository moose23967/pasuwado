from .randomizer import Randomizer


class Generator:
    def __init__(self, randomizer: Randomizer):
        self.randomizer = randomizer

    def generate(self, size: int) -> str:
        characters = [chr(i) for i in range(33, 127)]

        return "".join(
            [
                characters[
                    self.randomizer.generate_random_int_in_range(len(characters) - 1)
                ]
                for _ in range(size)
            ]
        )
