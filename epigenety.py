from instagrapi import Client
from info import *

class Epigenety:

    def __init__(self):
        self.client = Client()

    def connect(self):
        self.client.login(username=INSTA_USERNAME_PYTHON, password=INSTA_PASSWORD)

    def upload(self, path=None, caption=None, location=None):
        media = self.client.photo_upload(
            path=path,
            caption=caption,
            location=location
        )

        return media
