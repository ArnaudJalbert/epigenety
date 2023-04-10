from prompt import Prompt

import random


class Phase4(Prompt):

    PROMPT_FORMAT = "According to {}, what is the difference between the wilderness and nature."

    def __init__(self):
        super(Phase4, self).__init__()

        # path to the list of elements
        self.people_file = "./phase4/people.txt"

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
