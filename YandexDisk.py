class YaUploader:
    def __init__(self):
        pass

    def upload(self,  folder_path: str):

        import requests
        import json

        auth = {'Authorization': 'OAuth *****************'}
        response = requests.get(f'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=%2F{folder_path}',
                                headers=auth)

        upload_url = response.json()['href']
        print(upload_url)
        with open(folder_path) as f:
            file = f.read()
            up_response = requests.put(upload_url, data=file)


        return f'Файл {folder_path} успешно загружен.'


if __name__ == '__main__':
    uploader = YaUploader()
    result = uploader.upload('file_for_upload.txt')
    print(result)