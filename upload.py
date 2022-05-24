import requests
import os


class YAUpload:
    def __init__(self, token: str, version):
        self.files = None
        self.params = None
        self.path = None
        self.headers = None
        self.host = f'https://cloud-api.yandex.net:443/'
        self.token = token
        self.version = version

    def path_and_files_in(self):
        os.chdir('photos')
        path = os.path.join(os.getcwd())
        self.path = path
        self.files = os.listdir(self.path)

    def get_headers(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_params(self):
        self.params = {
            'overwrite': True,
            'path': self.path
        }

    def ya_folder(self):
        url = f'{self.host}{self.version}/disk/resources'
        response = requests.put(url, headers=self.headers, params={'path': 'Photo'})
        folder_link = response.json()
        print(response.status_code)
        print(response.json())