from repository.file_manager.base import BaseFileManager
from repository.file_manager.managers import CSVFileManager


class FileManagerFactory:
    @staticmethod
    def create(file_path: str):
        ext = file_path.split(".")[-1]
        managers = {manager.get_extension(): manager for manager in BaseFileManager.__subclasses__()}
        if ext not in managers:
            return CSVFileManager
        return managers[ext]
