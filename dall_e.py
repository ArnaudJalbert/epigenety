import openai
from info import OPENAI_API_KEY

from PIL import Image

import requests
import os
from pathlib import Path


class DallE:

    def __init__(self, folder_destination="./images"):
        self.open_ai = openai
        self.folder_destination = '/'.join([os.getcwd(), "images"])
        self.dalle_response = {}
        self.image_url = None
        self.prompt = str()

    def connect(self):
        self.open_ai.api_key = OPENAI_API_KEY

    def generate_image(self, prompt):
        """
        Returns url of the image generated from prompt
        :param prompt:  to be used
        :return: (str) url of the generated image
        """

        self.prompt = prompt

        # Make the API request
        self.dalle_response = openai.Image.create(
            prompt=self.prompt,
            n=1,
            size="1024x1024"
        )

        self.image_url = self.dalle_response["data"][0]["url"]

        return self.image_url

    def download_image(self):
        if self.image_url:

            img_data = requests.get(self.image_url).content

            file_name = '.'.join([self.prompt.replace(' ', '_').replace('.', ''), 'png'])

            path = '/'.join([self.folder_destination, file_name])

            with open(path, 'wb') as handler:
                handler.write(img_data)

            image = Image.open(path)
            image = image.convert("RGB")
            image.save(path.replace('.png', '.jpg'))

            return path.replace('.png', '.jpg')

        else:
            print("No image urls")

