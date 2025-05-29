import os

import pytest

DATA_DIR_NAME = "data"

@pytest.fixture
def current_dir():
    return os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def input_data_dir_path(current_dir) -> str:
    return os.path.join(current_dir, DATA_DIR_NAME)


@pytest.fixture
def input_data_paths(input_data_dir_path: str) -> list[str]:
    data_files = os.listdir(input_data_dir_path)
    test_data = [os.path.join(input_data_dir_path, file_name) for file_name in data_files]
    return test_data

@pytest.fixture
def output_data_path(tmp_path):
    return tmp_path / "report"
