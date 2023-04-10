from prompt import Prompt

import random


class Phase2(Prompt):

    PROMPT_FORMAT = "According to {}, is it natural for the human to alter its environment?" \
                    "is it still nature if the human has altered it in any way? Explain in details and give arguments."

    def __init__(self):
        super(Phase2, self).__init__()

        # path to the list of elements
        self.people_file = "./phase2/people.txt"

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
