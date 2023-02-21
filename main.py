from epigenety import Epigenety

from chat_gpt import ChatGPT
from dall_e import DallE

if __name__ == "__main__":

    prompt = "Lewis Hamilton eating a poutine"

    # generate the quote
    chat = ChatGPT()

    chat.connect()

    quote = chat.generate_quote(prompt)

    # generate the image
    dall_e = DallE()

    dall_e.connect()

    image = dall_e.generate_image(prompt)

    print(quote)
    print(image)

    # setting up the bot
    epigenety = Epigenety()

    epigenety.connect()

    epigenety.upload(image,quote)
