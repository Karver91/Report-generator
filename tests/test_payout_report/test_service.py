import os.path


def test_process(payout_service):
    __output_data_path = payout_service.repository.output
    payout_service.process()
    assert os.path.exists(__output_data_path)
