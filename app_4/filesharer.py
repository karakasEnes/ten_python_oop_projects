from filestack import Client
from dotenv import dotenv_values

class FileSharer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.api_key = dotenv_values('./.env')['FILESTACK_API_KEY']

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url
