import openai
from info import OPENAI_API_KEY

import openai
from info import OPENAI_API_KEY


class DallE:

    def __init__(self):
        self.open_ai = openai

    def connect(self):
        self.open_ai.api_key = OPENAI_API_KEY

    def generate_image(self, prompt):
        """
        Returns url of the image generated from prompt
        :param prompt:  to be used
        :return: (str) url of the generated image
        """

        # Make the API request
        dalle_response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )

        return dalle_response["data"][0]["url"]
