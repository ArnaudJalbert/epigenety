from epigenety import Epigenety

from chat_gpt import ChatGPT
from dall_e import DallE

from phase1.phase1 import Phase1

DESCRIPTION = "{quote} \n -{artist} \n\n Created with DALLE and ChatGPT from prompt: \" {prompt} \" "

if __name__ == "__main__":

    # generate the prompt
    prompt = Phase1()

    prompt.generate_prompt()

    print(prompt)

    # generate the quote
    chat = ChatGPT()

    chat.connect()

    quote = chat.generate_quote(prompt.prompt)

    print(quote)

    # generate the image
    dall_e = DallE()

    dall_e.connect()

    dall_e.generate_image(prompt.prompt)

    image_path = dall_e.download_image()

    print(image_path)

    # setting up the bot
    epigenety = Epigenety()

    epigenety.connect()

    description = DESCRIPTION.format(quote=quote, artist=prompt.artist, prompt=prompt)

    epigenety.upload(image_path,quote)
