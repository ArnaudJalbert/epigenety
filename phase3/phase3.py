from prompt import Prompt

import random


class Phase3(Prompt):

    PROMPT_FORMAT = "Demonstrate how the impact of the human has changed over time in the perspective of {}."

    def __init__(self):
        super(Phase3, self).__init__()

        # path to the list of elements
        self.people_file = "./phase3/people.txt"

        # chosen element to create the prompt
        self.person = str()

        self.prompt = str()

    def generate_prompt(self):

        # retrieving all the information from the files
        people = self.parse_keywords(self.people_file)

        # getting a random element from the list
        self.person = random.choice(people)

        self.prompt = self.PROMPT_FORMAT.format(self.person)

        return self.prompt
