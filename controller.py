from config import settings
from core.interfaces.service import BaseService
from core.interfaces.view import ViewInterface
from repository.base import Repository
from services.simple_service_factory import ServiceFactory


class ExecutionController:
    def __init__(
            self,
            report: str,
            view: ViewInterface,
            repository: Repository,
            service: BaseService = None
    ):
        service: type[BaseService] = self._get_service(service, report)

        self.view = view
        self.service: BaseService = service(repository=repository)
        self.print_to_display: bool = settings.print_to_display

    def run(self):
        data = self.service.process()
        if self.print_to_display:
            self.view.print_report(data)

    @staticmethod
    def _get_service(service, report):
        if service is None:
            service = ServiceFactory.create(report=report)
        return service
