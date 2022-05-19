from download import VKDownload

token = ''
version = '5.131'
vk_id = '552934290'

if __name__ == '__main__':
    download = VKDownload(token, version, vk_id)
    download.get_photo_list()
