from enum import Enum
from typing import Any
from uuid import UUID


class CustomCSV:
    def __init__(self, file, delimiter=','):
        self.file = file
        self.delimiter = delimiter

    def read(self) -> list[dict]:
        result = []
        data = self.file.read()
        rows = [tuple(d.split(self.delimiter)) for d in data.split("\n")]
        header = rows[0]
        for row in rows[1:]:
            if all(x == "" for x in row):
                continue
            if len(row) != len(header):
                raise ValueError(f"Длинна строки {row} не соответствует длине заголовка {header} "
                                 f"Убедитесь, что в строке не использованы символы-разделители")
            result.append(dict(zip(header, row)))
        return result

    def write(self, data: list[dict]):
        if not data:
            raise ValueError(f"Не удалось записать файл. Нет данных для записи")
        header = [self.__encode_value(x) for x in data[0].keys()]
        rows = [self.delimiter.join(header)]
        for item in data:
            values = [self.__encode_value(x) for x in item.values()]
            row = self.delimiter.join(values)
            rows.append(row)
        self.file.write("\n".join(rows))

    @staticmethod
    def __encode_value(value: Any) -> str:
        if value is None:
            return ""
        if isinstance(value, Enum):
            return str(value.value)
        if isinstance(value, UUID):
            return value.hex
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, (int, str, float)):
            return str(value)
        raise ValueError(
            f"Атрибут {value!r} типа {type(value).__name__!r}"
            f" не может быть приведен к строке"
        )