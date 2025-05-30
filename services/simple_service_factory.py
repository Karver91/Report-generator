from core.interfaces.service import BaseService
from services.worker_services import WorkerPayout  # noqa


class ServiceFactory:
    @staticmethod
    def create(report: str):
        services = {service.get_report_type(): service for service in BaseService.__subclasses__()}
        if report not in services:
            raise KeyError(f"Не найден тип отчета {report!r}. "
                           f"Возможные варианты {[key for key in services.keys()]}")
        return services[report]
