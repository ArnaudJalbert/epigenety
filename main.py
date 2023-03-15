from epigenety import Epigenety

from chat_gpt import ChatGPT
from dall_e import DallE

from phase1.phase1 import Phase1

DESCRIPTION = "{quote} \n -{artist} \n\n Created with DALLE and ChatGPT from prompt: \" {prompt} \" "

current_attempt = 0
MAX_ATTEMPTS = 10


def main():

    try:
        # setting up the bot
        epigenety = Epigenety()

        epigenety.connect()

        # generate the prompt
        prompt = Phase1()


        prompt.generate_prompt()



        # generate the quote
        chat = ChatGPT()

        chat.connect()

        quote = chat.generate_quote(prompt.prompt)

        # generate the image
        dall_e = DallE()

        dall_e.connect()

        dall_e.generate_image(prompt.prompt)

        image_path = dall_e.download_image()

        description = DESCRIPTION.format(quote=quote, artist=prompt.artist, prompt=prompt)

        epigenety.upload(image_path, description)

    except Exception:
        if current_attempt < 10:
            main()
        else:
            exit(1)



if __name__ == "__main__":
    main()

