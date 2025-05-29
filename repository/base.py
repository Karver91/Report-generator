import os.path

from config import settings
from core.interfaces.model import ModelInterface
from repository.file_manager.base import BaseFileManager
from repository.file_manager.simple_file_manager_factory import FileManagerFactory


class Repository:
    def __init__(
            self,
            files: list[str],
            report: str,
    ):
        self.files = files
        self.report = self.output_data_path(report)

    def reed_files(self):
        result = []
        for file in self.files:
            file_manager: type[BaseFileManager] = FileManagerFactory.create(file_path=file)
            fm_instance = file_manager(file_path=file)
            data = fm_instance.read_file()
            result.extend(data)
        return result

    def write_file(self, data: list[dict]):
        file_manager: type[BaseFileManager] = FileManagerFactory.create(file_path=settings.output_file_format)
        fm_instance = file_manager(file_path=self.report)
        fm_instance.write_file(data=data)

    @staticmethod
    def output_data_path(report):
        report_dir, report_file = os.path.split(report)
        if not report_file:
            raise ValueError(f"Не указано название файла в пути {report_dir!r}")
        if report_dir:
            if not os.path.exists(report_dir):
                raise ValueError(f"Директории {report_dir!r} не найдено")
            return report
        else:
            return os.path.join(settings.output_data_dir_path, report_file)
