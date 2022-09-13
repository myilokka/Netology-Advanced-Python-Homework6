import requests


class YandexDiskStrategy:
    def __init__(self, token):
        # self.token = input('Введите токен для ЯндексДиск: ')
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)}

    def create_folder(self):
        params = {'path': 'vk_photos'}
        headers = self.get_headers()
        res = requests.put(self.url, headers=headers, params=params)

        return res


if __name__ == '__main__':
    token = 'AQAAAAAbMAVUAAhKRUWp4aYYhkODvrV6JS-o7B4'
    example = YandexDiskStrategy(token)
    res = example.create_folder()
    print(res)
