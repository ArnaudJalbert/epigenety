from abc import abstractmethod


class Prompt:

    def __init__(self):
        self.prompt = str()

    @abstractmethod
    def generate_prompt(self):
        pass

    @staticmethod
    def parse_keywords(file_path=None):

        if file_path:

            with open(file_path, "r") as file:
                lines = file.readlines()

            return lines

        else:
            print(file_path, " is not a path.")

    def __str__(self):
        return self.prompt
