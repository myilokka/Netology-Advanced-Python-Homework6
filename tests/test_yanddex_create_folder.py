from Yandex_disk import YandexDiskStrategy
import pytest


class TestClass:

    def setup(self):
        self.token = 'AQAAAAAbMAVUAAhKRUWp4aYYhkODvrV6JS-o7B4'
        self.example = YandexDiskStrategy(self.token)

    def test_create_folder_good(self):
        result = self.example.create_folder()
        assert result.status_code == 201

    def test_create_folder_bad(self):
        result = self.example.create_folder()
        assert result.status_code == 409


if __name__ == '__main__':
    pytest.main()
