from abc import ABC, abstractmethod

from core.interfaces.model import ModelInterface


class ServiceInterface(ABC):
    @abstractmethod
    def process(self):
        raise NotImplementedError


class BaseService(ServiceInterface):
    @abstractmethod
    def process(self):
        raise NotImplementedError

    @staticmethod
    def _serialize_model(data: list[dict], model) -> list[ModelInterface]:
        return [model(**item) for item in data]

    @staticmethod
    def _deserialize_model(data: list[ModelInterface]) -> list[dict]:
        return [item.to_dict() for item in data]
