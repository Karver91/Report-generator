from abc import ABC, abstractmethod

from core.interfaces.model import ModelInterface


class ServiceInterface(ABC):
    __report_type = None

    @abstractmethod
    def process(self):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_report_type(cls):
        raise NotImplementedError


class BaseService(ServiceInterface):
    __report_type = None

    def __init__(self, repository):
        self.repository = repository

    @abstractmethod
    def process(self):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_report_type(cls):
        raise NotImplementedError

    @staticmethod
    def _serialize_model(data: list[ModelInterface]) -> list[dict]:
        return [item.to_dict() for item in data]

    @staticmethod
    def _deserialize_model(data: list[dict], model) -> list[ModelInterface]:
        return [model(**item) for item in data]
