import requests
import os


class YAUpload:
    def __init__(self, token: str, version):
        self.photo_path = None
        self.photos = None
        self.params = None
        self.path = os.getcwd()
        self.headers = None
        self.folder_link = None
        self.host = f'https://cloud-api.yandex.net:443/'
        self.token = token
        self.version = version

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
            response = requests.put(url, headers=self.headers, params=self.params)
            # get_link = response.json()
            # self.folder_link = get_link['href']
            # with open(self.path + '\\' + 'upl_link.txt', 'w') as file:
            #     file.write(get_link['href'])
        else:
            pass
        # with open(self.path + '\\' + 'upl_link.txt') as link:
        #     self.folder_link = link.readline()

    def ya_upload(self):
        for name in self.photos:
            with open(self.photo_path + '\\' + name, 'rb') as file:
                url = f'{self.host}{self.version}/disk/resources/upload'
                link = requests.get(url, headers=self.headers, params={'path': f'Photo/{name}', 'overwrite': True})
                upload = (link.json())['href']
                response = requests.put(upload, params={'path': f'Photo/{name}'})
                print(response.status_code)
