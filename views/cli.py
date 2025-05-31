from enum import Enum
from uuid import UUID

from core.interfaces.view import ViewInterface


class CLIView(ViewInterface):
    @classmethod
    def print_report(cls, data: list[dict]):
        if data:
            col_widths = cls.get_col_width(data)
            cls.print_table(col_widths, data)

    @classmethod
    def get_col_width(cls, data: list[dict]) -> dict[str, int]:
        headers = data[0].keys()
        col_widths = {header: len(header) for header in headers}
        for row in data:
            for header in headers:
                cell_value = cls.__encode_value(row[header])
                col_widths[header] = max(len(cell_value), col_widths[header])
        return col_widths

    @staticmethod
    def print_table(col_widths, data):
        headers = data[0].keys()
        # Создаем формат строки, используя спецификаторы выравнивания по левому краю "| {:<14} "
        row_format = " | ".join([f"{{:<{col_widths[header]}}}" for header in headers])
        separator = "-+-".join(["-" * col_widths[header] for header in headers])

        # Вызываем шаблон форматированной строки, передавая в него позиционные аргументы с помощью .format()
        print(row_format.format(*headers))
        print(separator)
        for row in data:
            values = [row[header] for header in headers]
            print(row_format.format(*values))

    @staticmethod
    def __encode_value(value) -> str:
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
