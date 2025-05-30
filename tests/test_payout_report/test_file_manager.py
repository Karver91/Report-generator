import os
from random import choice

import pytest

from repository.file_manager.managers import CSVFileManager, JSONFileManager
from repository.file_manager.simple_file_manager_factory import FileManagerFactory


@pytest.mark.parametrize(
    "manager",
    [CSVFileManager, JSONFileManager]
)
def test_write(input_data_dict, output_data_path, manager):
    manager(file_path=output_data_path).write_file(data=input_data_dict)
    assert os.path.exists(output_data_path)


@pytest.mark.parametrize(
    "ext, manager",
    [
        ("csv", CSVFileManager),
        ("json", JSONFileManager)
    ]
)
def test_read(input_data_paths, ext, manager):
    __file_path = choice([x for x in input_data_paths if x.endswith(ext)])
    result = manager(file_path=__file_path).read_file()
    assert len(result) > 0


def test_file_manager_factory(ext, manager):
    file_path = f"data.{ext}"
    result = FileManagerFactory.create(file_path=file_path)
    assert result == manager
