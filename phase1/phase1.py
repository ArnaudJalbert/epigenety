from prompt import Prompt

import random


class Phase1(Prompt):

    PROMPT_FORMAT = "{} in the {} during the {} painted by {} in a {} style."

    def __init__(self):
        super(Phase1, self).__init__()

        # path to the list of elements
        self.artists_file = "./phase1/artists.txt"
        self.animals_file = "./phase1/animals.txt"
        self.climates_file = "./phase1/climates.txt"
        self.eras_file = "./phase1/eras.txt"
        self.styles_file = "./phase1/styles.txt"

        # chosen element to create the prompt
        self.animal = str()
        self.climate = str()
        self.era = str()
        self.artist = str()
        self.style = str()

    def generate_prompt(self):

        # retrieving all the information from the files
        animals = self.parse_keywords(self.animals_file)
        climates = self.parse_keywords(self.climates_file)
        eras = self.parse_keywords(self.eras_file)
        artists = self.parse_keywords(self.artists_file)
        styles = self.parse_keywords(self.styles_file)

        # getting a random element from the list
        self.animal = random.choice(animals)
        self.climate = random.choice(climates)
        self.era = random.choice(eras)
        self.artist = random.choice(artists)
        self.style = random.choice(styles)

        self.prompt = self.PROMPT_FORMAT.format(self.animal, self.climate, self.era, self.artist, self.style)

        self.prompt = self.prompt.replace('\n', '')

        return self.prompt
