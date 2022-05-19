import requests
from pprint import pprint


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
        pprint(request)
