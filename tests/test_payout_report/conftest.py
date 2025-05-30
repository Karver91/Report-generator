import pytest

from core.interfaces.service import ServiceInterface
from models.base import Worker
from repository.base import Repository
from services.worker_services import WorkerPayout


@pytest.fixture
def payout_repository(input_data_paths, output_data_path):
    repository: Repository = Repository(files=input_data_paths, output=output_data_path)
    return repository


@pytest.fixture
def payout_service(payout_repository):
    service: ServiceInterface = WorkerPayout(repository=payout_repository)
    return service


@pytest.fixture
def input_data_dict():
    data = [
        {'department': 'Marketing',
         'email': 'alice@example.com',
         'hourly_rate': '50',
         'hours_worked': '160',
         'id': '1',
         'name': 'Alice Johnson'}
    ]
    return data


@pytest.fixture
def input_data_model(input_data_dict):
    data = [
        Worker(**data) for data in input_data_dict
    ]
    return data