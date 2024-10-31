class EnglishWordsDictionary:
    def __init__(self):
        data: str

        with open("./pasuwado/modules/english-words-dictionary.txt") as data_file:
            data = data_file.read()

        self.data = data
