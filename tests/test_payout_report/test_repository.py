import os

import pytest

from repository.base import Repository


def test_json_reed(payout_repository, input_data_paths):
    json_file = [x for x in input_data_paths if x.split(".")[-1] == "json"]
    payout_repository.files = json_file
    result = payout_repository.reed_files()
    assert len(result) > 0


def test_csv_reed(payout_repository, input_data_paths):
    csv_file = [x for x in input_data_paths if x.split(".")[-1] == "csv"]
    payout_repository.files = csv_file
    result = payout_repository.reed_files()
    assert len(result) > 0


def test_csv_and_json_reed(payout_repository, input_data_paths):
    payout_repository.files = input_data_paths
    result = payout_repository.reed_files()
    assert len(result) > 0


def test_write(payout_repository, input_data_dict):
    __output_data_path = payout_repository.report
    payout_repository.write_file(input_data_dict)
    assert os.path.exists(__output_data_path)


def test_create_repository_with_report_attr_no_file_name_error(input_data_paths, input_data_dir_path):
    output_data_path = os.path.join(input_data_dir_path, "")
    with pytest.raises(ValueError):
        Repository(files=input_data_paths, report=output_data_path)


def test_create_repository_with_report_attr_dir_notfound_error(input_data_paths, input_data_dir_path):
    output_data_path = "/some/non/existent/dir/data.json"
    with pytest.raises(ValueError):
        Repository(files=input_data_paths, report=output_data_path)
