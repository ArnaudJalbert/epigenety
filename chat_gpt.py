import openai
from info import OPENAI_API_KEY


class ChatGPT:

    def __init__(self):
        self.open_ai = openai

    def connect(self):
        self.open_ai.api_key = OPENAI_API_KEY

    def generate_quote(self, prompt):
        """
        Returns quote generated from prompt
        :param prompt:  to be used
        :return: (str) quote
        """

        chat_response = self.open_ai.Completion.create(
            engine="text-davinci-002",
            prompt="Give me a quote of" + str(prompt),
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        return chat_response["choices"][0]["text"]




