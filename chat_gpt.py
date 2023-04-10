import openai

from info import *


class ChatGPT:

    def __init__(self):
        self.open_ai = openai
        self.chat_response = dict()
        self.quote = str()

    def connect(self):
        self.open_ai.api_key = OPENAI_API_KEY

    def generate_quote(self, prompt):
        """
        Returns quote generated from prompt
        :param prompt:  to be used
        :return: (str) quote
        """

        self.chat_response = self.open_ai.Completion.create(
            engine="text-davinci-002",
            prompt=str(prompt) + " in at least 2000 characters but less than 2200. Add a warnign add the end that the essay is not real.",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        self.quote = self.chat_response["choices"][0]["text"]

        return self.quote





