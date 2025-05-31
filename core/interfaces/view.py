from abc import ABC, abstractmethod


class ViewInterface(ABC):
    @classmethod
    @abstractmethod
    def print_report(cls, data):
        raise NotImplementedError
