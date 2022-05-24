from download import VKDownload
from pprint import pprint

token = "a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd"
version = "5.131"
vk_id = "552934290"

if __name__ == "__main__":
    download = VKDownload(token, version, vk_id)
    json_list = download.get_photo_list()
    path = download.create_folder()
    download_dict = download.get_download_dict(json_list)
    log = download.download_and_log(download_dict, path)