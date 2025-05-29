from abc import abstractmethod

from core.interfaces.repository import FileManagerInterface


class BaseFileManager(FileManagerInterface):
    """Базовый класс для работы с файлом данных"""
    __extension = None

    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read_file(self) -> list:
        """Читает файл. Возвращает список объектов модели"""
        raise NotImplementedError

    @abstractmethod
    def write_file(self, data) -> None:
        """Записывает данные в файл"""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_extension(cls):
        raise NotImplementedError
