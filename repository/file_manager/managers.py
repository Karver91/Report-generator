import json

from repository.file_manager.base import BaseFileManager
from utils.csv import CustomCSV


class CSVFileManager(BaseFileManager):
    __extension = "csv"

    def __init__(self, file_path):
        super().__init__(file_path)

    def read_file(self) -> list:
        """Читает файл. Возвращает список данных"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = CustomCSV(file=file).read()
                return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.file_path!r} не найден")

    def write_file(self, data: list[dict]) -> None:
        """Записывает данные в файл"""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            CustomCSV(file=file).write(data)

    @classmethod
    def get_extension(cls):
        return cls.__extension


class JSONFileManager(BaseFileManager):
    __extension = "json"

    def __init__(self, file_path):
        super().__init__(file_path)

    def read_file(self) -> list:
        """Читает файл. Возвращает список данных"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []

    def write_file(self, data: list[dict]) -> None:
        """Записывает данные в файл"""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(obj=data, fp=file, ensure_ascii=False, indent=4)

    @classmethod
    def get_extension(cls):
        return cls.__extension


# ------------------------------------ Пример добавления нового менеджера ------------------------------------

class XMLFileManager(BaseFileManager):
    __extension = "xml"

    def __init__(self, file_path):
        super().__init__(file_path)

    def read_file(self) -> list:
        ...

    def write_file(self, data) -> None:
        ...

    @classmethod
    def get_extension(cls):
        return cls.__extension
