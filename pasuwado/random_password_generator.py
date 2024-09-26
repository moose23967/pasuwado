from .random_number_generator import RandomNumberGenerator


class RandomPasswordGenerator:
    def __init__(self, random_number_generator: RandomNumberGenerator):
        self.random_number_generator = random_number_generator

    def generate(self, size: int) -> str:
        characters = [chr(i) for i in range(33, 127)]

        return "".join(
            [
                characters[
                    self.random_number_generator.generate_random_int_in_range(
                        len(characters) - 1
                    )
                ]
                for _ in range(size)
            ]
        )
