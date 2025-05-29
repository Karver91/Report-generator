import os
from random import choice

from repository.file_manager.managers import CSVFileManager, JSONFileManager


def test_csv_write(input_data_dict, output_data_path):
    CSVFileManager(file_path=output_data_path).write_file(data=input_data_dict)
    assert os.path.exists(output_data_path)


def test_csv_read(input_data_paths):
    __file_path = choice([x for x in input_data_paths if x.endswith("csv")])
    result = CSVFileManager(file_path=__file_path).read_file()
    assert len(result) > 0


def test_json_write(input_data_dict, output_data_path):
    JSONFileManager(file_path=output_data_path).write_file(data=input_data_dict)
    assert os.path.exists(output_data_path)


def test_json_read(input_data_paths):
    __file_path = choice([x for x in input_data_paths if x.endswith("json")])
    result = JSONFileManager(file_path=__file_path).read_file()
    assert len(result) > 0
