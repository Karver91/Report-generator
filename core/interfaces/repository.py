from abc import ABC, abstractmethod


class FileManagerInterface(ABC):
    __extension = None

    @abstractmethod
    def read_file(self) -> list:
        raise NotImplementedError

    @abstractmethod
    def write_file(self, data) -> None:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_extension(cls):
        raise NotImplementedError