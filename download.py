import requests
import os


class VKDownload:

    def __init__(self, token, version, vk_id):
        self.token = token
        self.host = 'https://api.vk.com/method/'
        self.version = version
        self.id = vk_id

    def get_params(self):
        return {
            'access_token': self.token,
            'v': self.version,
            'owner_id': self.id,
            'album_id': 'profile',
            'rev': '1',
            'photo_sizes': '1',
            'extended': '1',
            'count': '5'
        }

    def get_photo_list(self):
        url = f'{self.host}photos.get'
        params = self.get_params()
        request = requests.get(url, params=params).json()
        return request

    def create_folder(self):
        if not os.path.isdir('photos'):
            os.mkdir('photos')
        os.chdir('photos')
        path = os.getcwd()
        return path

    def download_dict(self, json):
        d_dict = {}
        for item in json['response']['items']:
            name = item['likes']['count']
            date = item['date']
            largest_type = ''
            url = ''
            pixels = 0
            for size in item['sizes']:
                multiply = int(size['height']) * int(size['width'])
                if multiply > pixels:
                    pixels = multiply
                    largest_type = size['type']
                    url = size['url']
            if name in d_dict.keys():
                d_dict[str(name) + ' ' + str(date)] = [url, largest_type]
            else:
                d_dict[name] = [url, largest_type]
        return d_dict
