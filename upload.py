import requests
import os
from tqdm import tqdm


class YAUpload:
    def __init__(self, token: str, version):
        self.path = os.getcwd()
        self.host = f'https://cloud-api.yandex.net:443/'
        self.token = token
        self.version = version
        self.headers = None
        self.folder_link = None
        self.photo_path = None
        self.photos = None
        self.params = None

    def path_and_files_in(self):
        os.chdir('photos')
        path = os.path.join(os.getcwd())
        self.photo_path = path
        self.photos = os.listdir(self.photo_path)

    def get_headers(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_params(self):
        self.params = {
            'overwrite': True,
            'path': 'Photo'
        }

    def ya_folder(self):
        url = f'{self.host}{self.version}/disk/resources'
        search = requests.get(url, headers=self.headers, params=self.params)
        if search.status_code == 404:
            requests.put(url, headers=self.headers, params=self.params)

        else:
            pass

    def ya_upload(self):
        for name in tqdm(self.photos):
            with open(self.photo_path + '\\' + name, 'rb') as file:
                url = f'{self.host}{self.version}/disk/resources/upload'
                link = requests.get(url, headers=self.headers,
                                    params={'path': f'{self.params["path"]}/{name}', 'overwrite': True})
                upload = (link.json())['href']
                requests.put(upload, files={'file': file})
        print(f'Photos uploaded to folder {self.params["path"]} on YaDisk ')
