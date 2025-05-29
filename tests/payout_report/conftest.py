import pytest

from core.interfaces.service import ServiceInterface
from repository.base import Repository
from services.worker_services import WorkerPayout


@pytest.fixture
def payout_repository(input_data_paths, output_data_path):
    repository: Repository = Repository(files=input_data_paths, report=output_data_path)
    return repository


@pytest.fixture
def payout_service(payout_repository):
    service: ServiceInterface = WorkerPayout(repository=payout_repository)
    return service
