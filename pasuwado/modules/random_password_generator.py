from .english_words_dictionary import EnglishWordsDictionary
from .random_number_generator import RandomNumberGenerator


class RandomPasswordGenerator:
    def __init__(
        self,
        english_words_dictionary: EnglishWordsDictionary,
        random_number_generator: RandomNumberGenerator,
    ) -> None:
        self.english_words_dictionary = english_words_dictionary
        self.random_number_generator = random_number_generator

    def generate(self, length: int):
        english_words_dictionary_list = self.english_words_dictionary.data.split("\n")

        return "-".join(
            [
                english_words_dictionary_list[
                    self.random_number_generator.generate(
                        len(english_words_dictionary_list) - 1
                    )
                ]
                for _ in range(length)
            ]
        )
