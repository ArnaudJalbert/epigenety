from epigenety import Epigenety

from chat_gpt import ChatGPT
from dall_e import DallE

from phase1.phase1 import Phase1
from phase2.phase2 import Phase2
from phase3.phase3 import Phase3
from phase4.phase4 import Phase4
from phase5.phase5 import Phase5

DESCRIPTION = "{quote} \n -{person}"

current_attempt = 0
MAX_ATTEMPTS = 10


def main():

    print("Starting")
    # setting up the bot
    epigenety = Epigenety()

    epigenety.connect()
    print("Connected to instagram")

    # generate the prompt
    prompt = Phase5()

    prompt.generate_prompt()
    print("Prompt generated")

    print(prompt.prompt)

    # generate the quote
    chat = ChatGPT()

    chat.connect()

    quote = chat.generate_quote(prompt.prompt)
    print("Quote generated")

    # generate the image
    dall_e = DallE()

    dall_e.connect()

    dall_e.generate_image(prompt)

    print("Image generated")

    image_path = dall_e.download_image()

    description = DESCRIPTION.format(quote=quote, person=prompt.person)

    epigenety.upload(image_path, description)
    print("Post uploaded")


if __name__ == "__main__":
    main()

