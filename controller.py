from core.interfaces.service import BaseService
from repository.base import Repository
from services.simple_service_factory import ServiceFactory


class ExecutionController:
    def __init__(
            self,
            report: str,
            repository: Repository,
            service: BaseService = None
    ):
        service: type[BaseService] = self._get_service(service, report)
        self.service: BaseService = service(repository=repository)

    def run(self):
        self.service.process()

    @staticmethod
    def _get_service(service, report):
        if service is None:
            service = ServiceFactory.create(report=report)
        return service
