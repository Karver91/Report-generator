from core.interfaces.model import ModelInterface


class Worker(ModelInterface):
    _KEY_MAPPING = {
        "hourly_rate": "rate",
        "salary": "rate",
        "hours_worked": "hours"
    }

    def __init__(self, *args, **kwargs):
        if args:
            raise ValueError("В инициализатор ожидаются именованные аргументы")
        for old_key, new_key in self._KEY_MAPPING.items():
            if old_key in kwargs:
                kwargs[new_key] = kwargs.pop(old_key)

        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.department = kwargs.get('department')
        self.hours = kwargs.get('hours')
        self.rate = kwargs.get('rate')

    def __setattr__(self, key, value):
        value = self.validate(key, value)
        super().__setattr__(key, value)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "hours": self.hours,
            "rate": self.rate
        }

    def validate(self, key, value):
        if key in ("id", "hours", "rate"):
            value = self.__int_gt_0(key, value)
        return value

    @staticmethod
    def __int_gt_0(key, value):
        try:
            if not isinstance(value, int):
                value = int(value)
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            raise ValueError(f"'{key}={value}' Значение ключа не является числом, либо меньше 0")
