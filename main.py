from download import VKDownload
from upload import YAUpload

vk_token = "a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd"
vk_version = "5.131"
vk_id = "552934290"

ya_token = 'AQAAAAAJ2bXkAADLW5INLqBOyUuEuFH8gSu4M3k'
ya_version = 'v1'

if __name__ == "__main__":
    download = VKDownload(vk_token, vk_version, vk_id)
    download.get_photo_list()
    download.create_folder()
    download.get_download_dict()
    download.download_and_log()
    upload = YAUpload(ya_token, ya_version)
    upload.path_and_files_in()
    upload.get_headers()
    upload.get_params()
    upload.ya_folder()
    upload.ya_upload()

