from abc import ABC, abstractmethod


class ModelInterface(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def validate(self, key, value):
        raise NotImplementedError
