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
